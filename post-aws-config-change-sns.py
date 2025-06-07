import json
import os
import boto3
import time
from datetime import datetime, timedelta

# Initialize clients outside the handler for better performance (warm starts)
sns_client = boto3.client('sns')
dynamodb_client = boto3.client('dynamodb')
cloudtrail_client = boto3.client('cloudtrail') 

def get_cloudtrail_event_identity(config_event_detail):
    """
    Attempts to find the userIdentity from a CloudTrail event that likely
    caused the Config change. Prioritizes relatedEvents, falls back to lookup_events.
    """
    user_identity_details = {
        'userName': 'Unknown',
        'type': 'N/A',
        'arn': 'N/A',
        'principalId': 'N/A',
        'accountId': 'N/A',
        'sessionContext': {},
        'cloudTrailEventId': 'N/A' # Initialize for consistency
    }

    # 1. Try to find eventID in relatedEvents (most reliable)
    related_events = config_event_detail.get('configurationItem', {}).get('relatedEvents', [])
    for event_ref in related_events:
        if 'eventID' in event_ref:
            user_identity_details['cloudTrailEventId'] = event_ref['eventID']
            print(f"INFO: Found CloudTrail event ID '{user_identity_details['cloudTrailEventId']}' in Config event relatedEvents.")
            # If Config provides a direct event ID, this is usually sufficient.
            # We don't typically get the full userIdentity from here without a lookup.
            # For a truly complete identity, you'd need the full CloudTrail event.
            # This is where the tradeoff lies: lookup_events (cost/latency) vs. unknown identity.
            return user_identity_details # Return what we have from relatedEvents

    print("INFO: No CloudTrail event ID found in Config event's relatedEvents. Attempting lookup_events.")

    # 2. Fallback: Use lookup_events if relatedEvents is empty
    try:
        resource_arn = config_event_detail.get('configurationItem', {}).get('ARN', 'N/A')
        capture_time_str = config_event_detail.get('configurationItem', {}).get('configurationItemCaptureTime', 'N/A')
        resource_type = config_event_detail.get('configurationItem', {}).get('resourceType', 'N/A')

        if resource_arn == 'N/A' or capture_time_str == 'N/A':
            print("WARNING: Missing resource ARN or capture time for lookup_events.")
            return user_identity_details # Return default unknown

        capture_time = datetime.fromisoformat(capture_time_str.replace('Z', '+00:00'))

        # Define a time window to search for CloudTrail events (e.g., 5 minutes before and after)
        # Adjust timedelta as needed based on observed Config propagation delays
        start_time = capture_time - timedelta(minutes=5)
        end_time = capture_time + timedelta(minutes=5)

        # Extract resource identifier for lookup_events. This can be tricky.
        # For EC2 instance changes, sometimes the InstanceId, or VolumeId is directly referenced.
        cloudtrail_resource_id = config_event_detail.get('configurationItem', {}).get('resourceId', 'N/A')
        if cloudtrail_resource_id == 'N/A' and 'Relationships' in config_event_detail.get('configurationItemDiff', {}).get('changedProperties', {}):
             # Try to get the associated instance ID if this is an attachment change (like your example)
             # This parsing needs to be robust for various change types
             updated_rel = config_event_detail['configurationItemDiff']['changedProperties'].get('Relationships.0', {}).get('updatedValue', {})
             if updated_rel.get('resourceType') == 'AWS::EC2::Instance':
                 cloudtrail_resource_id = updated_rel.get('resourceId')
                 print(f"INFO: Derived resourceId for lookup from Relationships: {cloudtrail_resource_id}")


        # Map AWS Config resource types to CloudTrail event sources and potential event names
        cloudtrail_event_source = None
        # Common event names that cause configuration changes for EC2 instance/volume
        relevant_event_names = []

        if resource_type == 'AWS::EC2::Instance':
            cloudtrail_event_source = 'ec2.amazonaws.com'
            relevant_event_names = [
                "RunInstances", "StopInstances", "StartInstances", "TerminateInstances",
                "ModifyInstanceAttribute", "AttachVolume", "DetachVolume",
                "AssociateIamInstanceProfile", "DisassociateIamInstanceProfile",
                "CreateTags", "DeleteTags" # For tag changes
            ]
        elif resource_type == 'AWS::EC2::Volume':
            cloudtrail_event_source = 'ec2.amazonaws.com'
            relevant_event_names = [
                "CreateVolume", "DeleteVolume", "AttachVolume", "DetachVolume",
                "ModifyVolume", "CreateTags", "DeleteTags" # For tag changes
            ]
        # Add more mappings for other resource types (ALB, RDS, CloudFront, WAF, etc.)
        # elif resource_type == 'AWS::ElasticLoadBalancingV2::LoadBalancer':
        #     cloudtrail_event_source = 'elasticloadbalancing.amazonaws.com'
        #     relevant_event_names = ["ModifyLoadBalancerAttributes", "SetSecurityGroups", ...]
        # ... and so on

        if not cloudtrail_event_source or not relevant_event_names:
            print(f"WARNING: No CloudTrail event source or relevant event names mapping for resource type: {resource_type}")
            return user_identity_details # Return default unknown

        lookup_attributes = [
            {'AttributeKey': 'ResourceName', 'AttributeValue': cloudtrail_resource_id},
            {'AttributeKey': 'EventSource', 'AttributeValue': cloudtrail_event_source}
        ]
        # If the resource name for lookup is too generic (e.g., 'volume'),
        # or if the API call doesn't always include the resource ID in ResourceName,
        # you might need to adjust lookup_attributes or further filter results.

        print(f"INFO: Calling CloudTrail lookup_events with attributes: {lookup_attributes} "
              f"between {start_time} and {end_time}")

        response = cloudtrail_client.lookup_events(
            LookupAttributes=lookup_attributes,
            StartTime=start_time,
            EndTime=end_time,
            MaxResults=50
        )

        for event_record in response.get('Events', []):
            cloudtrail_event = json.loads(event_record['CloudTrailEvent'])
            
            # Additional checks for a more confident match:
            # 1. EventName must be one of the relevant ones
            if cloudtrail_event.get('eventName') not in relevant_event_names:
                continue

            # 2. Ensure it's not a service or automated call (unless you want to track those)
            if cloudtrail_event.get('userIdentity', {}).get('type') in ['AWSService', 'Service']:
                continue
            
            # 3. (Optional but good) Check if requestParameters contains the relevant IDs
            # This is highly specific to each API call's structure
            # For AttachVolume, requestParameters would have 'volumeId' and 'instanceId'
            request_parameters = cloudtrail_event.get('requestParameters', {})
            if resource_type == 'AWS::EC2::Instance' and cloudtrail_event.get('eventName') == 'AttachVolume':
                if request_parameters.get('instanceId') != cloudtrail_resource_id and request_parameters.get('volumeId') != config_event_detail.get('configurationItemDiff', {}).get('changedProperties', {}).get('Relationships.0', {}).get('updatedValue', {}).get('resourceId'):
                     continue # Not the right attachment event for this instance
            elif resource_type == 'AWS::EC2::Volume' and cloudtrail_event.get('eventName') == 'AttachVolume':
                 if request_parameters.get('volumeId') != cloudtrail_resource_id:
                     continue # Not the right attachment event for this volume


            user_identity = cloudtrail_event.get('userIdentity', {})
            if user_identity:
                print(f"INFO: Found matching CloudTrail event: {event_record['EventName']} by {user_identity.get('userName', 'N/A')}")
                user_identity_details['userName'] = user_identity.get('userName', 'N/A')
                user_identity_details['type'] = user_identity.get('type', 'N/A')
                user_identity_details['arn'] = user_identity.get('arn', 'N/A')
                user_identity_details['principalId'] = user_identity.get('principalId', 'N/A')
                user_identity_details['accountId'] = user_identity.get('accountId', 'N/A')
                user_identity_details['sessionContext'] = user_identity.get('sessionContext', {})
                user_identity_details['cloudTrailEventId'] = event_record['EventId'] # Overwrite if found

                return user_identity_details

        print("INFO: No direct matching CloudTrail event found within the time window after lookup_events.")
        return user_identity_details # Return with default unknown identity

    except Exception as e:
        print(f"WARNING: Error during CloudTrail lookup_events: {e}")
        return user_identity_details # Return with default unknown identity


def lambda_handler(event, context):
    """
    AWS Lambda function to process AWS Config Configuration Item Change events.
    It filters events based on a 'System: ProdCore' tag, attempts to find the
    related CloudTrail event ID, records the change in DynamoDB, and publishes
    a formatted message to an SNS topic.
    """
    # --- Configuration from Environment Variables ---
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME') # This should be 'UnifiedConfigTrailLog'
    target_tag_key = os.environ.get('TARGET_TAG_KEY', 'System')
    target_tag_value = os.environ.get('TARGET_TAG_VALUE', 'ProdCore')

    if not sns_topic_arn:
        print("ERROR: SNS_TOPIC_ARN environment variable not set. Cannot publish notification.")
        return {'statusCode': 500, 'body': json.dumps('SNS_TOPIC_ARN not configured.')}
    if not dynamodb_table_name:
        print("ERROR: DYNAMODB_TABLE_NAME environment variable not set. Cannot record in DynamoDB.")
        return {'statusCode': 500, 'body': json.dumps('DYNAMODB_TABLE_NAME not configured.')}

    try:
        # The main 'detail' object from the EventBridge event
        
        detail = event.get('detail', {})

        # --- Extracting core event metadata ---
        event_id = event.get('id', 'N/A') # EventBridge event ID
        event_time = event.get('time', 'N/A') # Timestamp from EventBridge
        aws_account_id = event.get('account', 'N/A')
        aws_region_event = event.get('region', 'N/A') # Region where the event originated

        # --- Extracting resource identification from configurationItem ---
        config_item = detail.get('configurationItem', {})
        resource_id = config_item.get('resourceId', 'N/A')
        resource_type = config_item.get('resourceType', 'N/A')
        resource_arn = config_item.get('ARN', 'N/A')
        aws_region_resource = config_item.get('awsRegion', 'N/A') # Region of the resource itself
        resource_tags = config_item.get('tags', {}) # Get the dictionary of tags

        # --- Tag-Based Filtering ---
        if resource_tags.get(target_tag_key) != target_tag_value:
            print(f"INFO: Resource {resource_id} (Type: {resource_type}) does not have the target tag "
                  f"'{target_tag_key}:{target_tag_value}'. Skipping notification and DB record.")
            return {'statusCode': 200, 'body': json.dumps('Resource not matching target tag.')}

        # --- Extracting what changed ---
        config_diff = detail.get('configurationItemDiff', {})
        overall_change_type = config_diff.get('changeType', 'N/A')
        changed_properties = config_diff.get('changedProperties', {})
        capture_time = config_item.get('configurationItemCaptureTime', 'N/A')

        # --- NEW: Get CloudTrail event ID and user identity (best effort) ---
        time.sleep(30) 
        print(f"INFO: detail is : {json.dumps(detail)}")
        user_identity_details = get_cloudtrail_event_identity(detail)
        who_made_change = "Unknown (CloudTrail correlation not available)"
        cloudtrail_event_id_for_db = "N/A"

        if user_identity_details:
            cloudtrail_event_id_for_db = user_identity_details.get('cloudTrailEventId', 'N/A')
            if user_identity_details.get('userName') != 'Unknown': # If a specific user was found
                who_made_change = f"{user_identity_details.get('userName', 'N/A')} (Type: {user_identity_details.get('type', 'N/A')}, ARN: {user_identity_details.get('arn', 'N/A')})"
            elif cloudtrail_event_id_for_db != 'N/A': # We found the ID, but not full identity in Config event
                who_made_change = f"Correlated by CloudTrail Event ID: {cloudtrail_event_id_for_db}"


        # --- Prepare data for DynamoDB ---
        item_to_put = {
            'ResourceARN': {'S': resource_arn}, # Partition Key
            'ChangeTimestamp': {'S': capture_time}, # Sort Key
            'ResourceId': {'S': resource_id}, # For convenience, could be GSI if needed
            'ResourceType': {'S': resource_type},
            'RegionEvent': {'S': aws_region_event},
            'AwsAccountId': {'S': aws_account_id},
            'OverallChangeType': {'S': overall_change_type},
            'NotificationTime': {'S': event_time},
            'CloudTrailEventId': {'S': cloudtrail_event_id_for_db}, # New attribute for correlation
            'ChangedBy': {'S': who_made_change}, # The best effort "who" string
            'ResourceTags': {'S': json.dumps(resource_tags)},
            'ChangedProperties': {'S': json.dumps(changed_properties)},
            'FullConfigEvent': {'S': json.dumps(event)} # Store full original event for audit
        }
        if user_identity_details: # Add full identity if it was found
            item_to_put['UserIdentityDetails'] = {'S': json.dumps(user_identity_details)}


        # --- Record in DynamoDB ---
        print(f"Recording change for {resource_type} {resource_id} (Event ID: {cloudtrail_event_id_for_db}) in DynamoDB table {dynamodb_table_name}")
        dynamodb_client.put_item(
            TableName=dynamodb_table_name,
            Item=item_to_put
        )
        print("Successfully recorded in DynamoDB.")


        # --- Format the Useful Information for SNS ---
        message_subject = f"🚨 PROD CONFIG CHANGE: {resource_type} {resource_id} - {overall_change_type} by {who_made_change.split('(')[0].strip()}"
        if "Unknown" in who_made_change: # Shorten subject if identity isn't clear
            message_subject = f"🚨 PROD CONFIG CHANGE: {resource_type} {resource_id} - {overall_change_type}"


        message_body = []
        message_body.append(f"**Production Resource Configuration Change Detected!**")
        message_body.append("-" * 60)
        message_body.append(f"**Resource Type:** {resource_type}")
        message_body.append(f"**Resource ID:** {resource_id}")
        message_body.append(f"**ARN:** {resource_arn}")
        message_body.append(f"**AWS Account ID:** {aws_account_id}")
        message_body.append(f"**Resource Region:** {aws_region_resource}")
        message_body.append(f"**Overall Change Type:** {overall_change_type}")
        message_body.append(f"**Change Captured At:** {capture_time} (UTC)")
        message_body.append(f"**Changed By:** {who_made_change}") # Added who made the change
        if cloudtrail_event_id_for_db != 'N/A':
             message_body.append(f"**CloudTrail Event ID:** {cloudtrail_event_id_for_db}") # Added CloudTrail Event ID
        message_body.append(f"**Resource Tags:** {json.dumps(resource_tags, indent=2)}")
        message_body.append("-" * 60)

        if changed_properties:
            message_body.append("**Specific Property Changes:**")
            for prop_key, prop_details in changed_properties.items():
                change_type = prop_details.get('changeType', 'N/A')
                previous_value = prop_details.get('previousValue', 'N/A')
                updated_value = prop_details.get('updatedValue', 'N/A')

                if isinstance(previous_value, dict) or isinstance(previous_value, list):
                    previous_value = json.dumps(previous_value, indent=2)
                if isinstance(updated_value, dict) or isinstance(updated_value, list):
                    updated_value = json.dumps(updated_value, indent=2)

                message_body.append(f"- **Property:** `{prop_key}`")
                message_body.append(f"  **Change Type:** {change_type}")
                message_body.append(f"  **Previous Value:** {previous_value}")
                message_body.append(f"  **Updated Value:** {updated_value}")
            message_body.append("-" * 60)
        else:
            message_body.append("No specific property changes detailed in 'changedProperties'.")
            message_body.append("-" * 60)

        message_body.append(f"Event ID (Config): {event_id}")
        message_body.append("For full event details, check CloudWatch Logs for this Lambda invocation or query DynamoDB.")
        message_body.append(f"Record stored in DynamoDB table: {dynamodb_table_name}")

        final_message = "\n".join(message_body)

        # --- Publish to SNS Topic ---
        print(f"Publishing message to SNS Topic: {sns_topic_arn}")
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=message_subject,
            Message=final_message
        )
        print("Successfully published to SNS.")

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed Config change notification and recorded in DB.')
        }

    except Exception as e:
        error_message = f"ERROR: Failed to process event. Exception: {e}\nFull event received:\n{json.dumps(event, indent=2)}"
        print(error_message)
        try:
            sns_client.publish(
                TopicArn=sns_topic_arn,
                Subject=f"ERROR in Config Change Notifier Lambda for account {aws_account_id}",
                Message=error_message
            )
        except Exception as sns_err:
            print(f"CRITICAL ERROR: Failed to publish error message to SNS: {sns_err}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to process event: {e}")
        }

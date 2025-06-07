import json
import os
import boto3
from datetime import datetime

# Initialize clients outside the handler for better performance (warm starts)
sns_client = boto3.client('sns')
dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    """
    AWS Lambda function to process AWS Config Configuration Item Change events.
    It filters events based on a 'System: ProdCore' tag, publishes a formatted
    message to an SNS topic, and records the change in DynamoDB.
    """
    # --- Configuration from Environment Variables ---
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME')
    target_tag_key = os.environ.get('TARGET_TAG_KEY', 'System')
    target_tag_value = os.environ.get('TARGET_TAG_VALUE', 'ProdCore')

    if not sns_topic_arn:
        print("ERROR: SNS_TOPIC_ARN environment variable not set. Cannot publish notification.")
        # We might still want to log to DynamoDB even if SNS fails, or vice-versa
        return {
            'statusCode': 500,
            'body': json.dumps('SNS_TOPIC_ARN not configured.')
        }
    if not dynamodb_table_name:
        print("ERROR: DYNAMODB_TABLE_NAME environment variable not set. Cannot record in DynamoDB.")
        # This is a critical dependency, so we'll likely exit or just skip DynamoDB for this run
        return {
            'statusCode': 500,
            'body': json.dumps('DYNAMODB_TABLE_NAME not configured.')
        }

    try:
        print(f"INFO: Received event: {json.dumps(event)}")
        # The main 'detail' object from the EventBridge event
        detail = event.get('detail', {})

        # --- Extracting core event metadata ---
        event_id = event.get('id', 'N/A')
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
            return {
                'statusCode': 200,
                'body': json.dumps('Resource not matching target tag.')
            }

        # --- Extracting what changed ---
        config_diff = detail.get('configurationItemDiff', {})
        overall_change_type = config_diff.get('changeType', 'N/A')
        changed_properties = config_diff.get('changedProperties', {})

        # Extracting timestamps
        capture_time = config_item.get('configurationItemCaptureTime', 'N/A')

        # --- Prepare data for DynamoDB ---
        # DynamoDB doesn't directly support nested dictionaries for all attributes,
        # so we'll store changed_properties as a JSON string.
        # Also, DynamoDB doesn't store empty strings by default if you use put_item directly.
        # For this use case, we'll convert all values to strings for simplicity.
        item_to_put = {
            'ResourceId': {'S': resource_id},
            'ChangeTimestamp': {'S': capture_time}, # Use Config capture time as sort key
            'EventType': {'S': event['detail-type']},
            'Source': {'S': event['source']},
            'AccountId': {'S': aws_account_id},
            'RegionEvent': {'S': aws_region_event},
            'ResourceType': {'S': resource_type},
            'ResourceARN': {'S': resource_arn},
            'ResourceRegion': {'S': aws_region_resource},
            'OverallChangeType': {'S': overall_change_type},
            'NotificationTime': {'S': event_time}, # EventBridge time
            'ConfigurationItemCaptureTime': {'S': capture_time},
            'ResourceTags': {'S': json.dumps(resource_tags)}, # Store tags as JSON string
            'ChangedProperties': {'S': json.dumps(changed_properties)} # Store diff as JSON string
        }

        # --- Record in DynamoDB ---
        print(f"Recording change for {resource_type} {resource_id} in DynamoDB table {dynamodb_table_name}")
        dynamodb_client.put_item(
            TableName=dynamodb_table_name,
            Item=item_to_put
        )
        print("Successfully recorded in DynamoDB.")


        # --- Format the Useful Information for SNS (similar to before) ---
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

        message_body.append(f"Full Event ID: {event_id}")
        message_body.append("For full event details, check CloudWatch Logs for this Lambda invocation.")
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
        # Attempt to publish an error notification even if the main logic fails
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

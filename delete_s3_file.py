import boto3
from datetime import datetime, timedelta
from datetime import timezone
import time 
from botocore.exceptions import ClientError

# Initialize boto3 clients
dynamodb = boto3.client('dynamodb',region_name='ap-southeast-2')
s3 = boto3.client('s3',region_name='ap-southeast-2')
dynamodb_resource  = boto3.resource('dynamodb', region_name='ap-southeast-2')
# DynamoDB table name
table_name = 'RetentionPolicy'
log_table = 'deleted_files_log_table'
# Fetch retention policies from DynamoDB

def is_s3_folder(object_dict):
    # Check if the object's key ends with a '/'
    return object_dict['Key'].endswith('/')


def fetch_retention_policies():
    response = dynamodb.scan(TableName=table_name)
    return response['Items']

# Convert DynamoDB item to a Python dictionary
def convert_item(item):
    return {
        'bucket_name': item['bucket_name']['S'],
        'folder_prefix': item['folder_prefix']['S'],
        'retention_days': int(item['retention_days']['N'])
    }

# Delete old files based on retention policy using paginator

def delete_old_files(bucket, prefix, cutoff_date):
    
    deleted = 0
    keeped = 0
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)
    table = dynamodb_resource.Table(log_table)
    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                last_modified = obj['LastModified']
                last_modified_no_tz = last_modified.replace(tzinfo=None)

                #print (cutoff_date)
                #print (last_modified_no_tz)
               
                #cutoff_date_new=datetime.strptime(cutoff_date, "%Y-%m-%d %H:%M:%S")
                #last_modified_utc_new=datetime.fromisoformat(cutoff_date)
                #print (cutoff_date_new)
                #print (last_modified_utc_new)
                if last_modified_no_tz < cutoff_date:
                    if is_s3_folder(obj):
                        print(f"{obj['Key']} is a folder. keep all folders")
                    else:
                        file_key = obj['Key']
                        #print(f"Deleting {file_key} (Last modified: {last_modified})")
                        deleted += 1
                        file_dir = bucket + '/' + prefix 

                        item = {
                            'file_dir': file_dir,
                            'file_name': file_key,
                            'last_modified_time': last_modified_no_tz.strftime('%Y-%m-%d %H:%M:%S'),
                            'deleted_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            # add more attributes as needed
                        }
                        #print (item)
                        table.put_item(Item=item)
                        try:
                            s3.delete_object(Bucket=bucket, Key=file_key)
                        except ClientError as e:
                        # Handle the error and continue
                            print(f"Error deleting {bucket} {file_key}: {e}")
                            continue
                else:
                    print(f"Keeping {obj['Key']} (Last modified: {last_modified})")
                    keeped += 1
    print(f"total deleted {deleted} in bucket {bucket} / folder {prefix}")
    print(f"total keeped {keeped}   in bucket {bucket} / folder {prefix}")
def main():
    start_time = time.time()
    policies = fetch_retention_policies()
    for item in policies:
        policy = convert_item(item)
        print(policy)
        bucket_name = policy['bucket_name']
        folder_prefix = policy['folder_prefix']
        retention_days = policy['retention_days']
        
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        print(f"Processing bucket: {bucket_name}, folder: {folder_prefix}, retention days: {retention_days}")
        
        delete_old_files(bucket_name, folder_prefix, cutoff_date)
    
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    print("Deletion process completed.")


if __name__ == "__main__":
    main()
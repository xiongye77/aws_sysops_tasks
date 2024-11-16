import json
import boto3
import os
from botocore.exceptions import ClientError 

ecs_client = boto3.client('ecs')
s3_client = boto3.client('s3')
secretsmanager_client = boto3.client('secretsmanager')

def lambda_handler(event, context):
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))

    # Extract bucket name and key from the S3 event
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
    except Exception as e:
        print(f"Error extracting bucket or key: {e}")
        raise e

    # Optional: Check file size and decide whether to process
    # object_size = event['Records'][0]['s3']['object']['size']
    # if object_size < some_threshold:
    #     # Process directly in Lambda if small
    #     pass

    # ECS Task configuration
    cluster = os.environ.get('ECS_CLUSTER_NAME')
    task_definition = os.environ.get('ECS_TASK_DEFINITION')
    launch_type = 'FARGATE'
    #subnets = os.environ.get('SUBNETS').split(',')
    #security_groups = os.environ.get('SECURITY_GROUPS').split(',')
    container_name = os.environ.get('CONTAINER_NAME')

    # Role ARN for task execution (needs iam:PassRole permission)
    #task_execution_role_arn = os.environ.get('TASK_EXECUTION_ROLE_ARN')
    secret_name = os.environ.get('SECRET_NAME')
    #print (secret_name)
    try:
        get_secret_value_response = secretsmanager_client.get_secret_value(
            SecretId=secret_name
        )

        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            rds_credentials = json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            rds_credentials = json.loads(decoded_binary_secret)

        # Debug: Print retrieved credentials (Do not print sensitive data in production)
        print(rds_credentials)

    except ClientError as e:
        print(f"Error retrieving secret {secret_name}: {e}")
        raise e

    # Run ECS Task
    try:
        response = ecs_client.run_task(
            cluster=cluster,
            launchType=launch_type,
            taskDefinition=task_definition,
            overrides={
                'containerOverrides': [
                    {
                        'name': container_name,
                        'environment': [
                            {'name': 'S3_BUCKET', 'value': bucket},
                            {'name': 'S3_KEY', 'value': key},
                            {'name': 'RDS_HOST', 'value': rds_credentials['host']},
                            {'name': 'RDS_DATABASE', 'value': rds_credentials['database']},
                            {'name': 'RDS_USERNAME', 'value': rds_credentials['username']},
                            {'name': 'RDS_PASSWORD', 'value': rds_credentials['password']}
                        ]
                    }
                ]
            },
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0947ba18784781b1b'],
                    'securityGroups': ['sg-06251bea92f608abd'],
                    'assignPublicIp': 'DISABLED'
                }
            }
        )

        print(f"ECS Task started: {response['tasks'][0]['taskArn']}")

        return {
            'statusCode': 200,
            'body': json.dumps('ECS task started successfully')
        }

    except Exception as e:
        print(f"Error starting ECS task: {e}")
        raise e







sh-4.2$ more process_file.py 
import os
import boto3
import pandas as pd
from sqlalchemy import create_engine
def main():
    s3_bucket = os.environ.get('S3_BUCKET')
    s3_key = os.environ.get('S3_KEY')
    rds_host = os.environ.get('RDS_HOST')
    print(f"rds host is {rds_host}")
    rds_username = os.environ.get('RDS_USERNAME')
    rds_password = os.environ.get('RDS_PASSWORD')
    rds_database = os.environ.get('RDS_DATABASE')
    if not s3_bucket or not s3_key:
        print("S3_BUCKET or S3_KEY environment variable not set.")
        return

    s3_client = boto3.client('s3')

    try:
        # Download the file
        local_filename = '/tmp/' + os.path.basename(s3_key)
        s3_client.download_file(s3_bucket, s3_key, local_filename)
        print(f"Downloaded {s3_key} from bucket {s3_bucket} to {local_filename}")
        
        df = pd.read_csv(local_filename)
        print("Data Summary:")
        print(df.describe())
        # Process the file (placeholder for your logic)
        process_large_file(local_filename,rds_host, rds_username, rds_password, rds_database)

        # Optional: Upload results to S3 or another service

    except Exception as e:
        print(f"Error processing file: {e}")

def process_large_file(file_path,rds_host, rds_username, rds_password, rds_database):
    # Your processing logic here
    print(f"Processing file: {file_path}")
    # Simulate long-running task
    #import time
    #time.sleep(900)  # Sleep for 15 minutes
    print(f"rds host in process_large_file  is {rds_host}")
    print(f"rds username in process_large_file  is {rds_username}")
    print(f"rds password in process_large_file  is {rds_password}")
    engine = create_engine(f'postgresql+psycopg2://{rds_username}:{rds_password}@{rds_host}:5432/{rds_database}?sslmode=require')

    # CSV file without headers
    csv_file_path = file_path
    column_names = ["date",
             "month_year",
             "visitdatelocal",
             "visitweek",
             "visitmonth",
             "country",
             "countryiso",
             "region",
             "channel_group",
             "source",
             "campaign",
             "devicecategory",
             "medium",
             "landingpage",
             "exit_page",
             "client_id",
             "session_id",
             "session_duration",
             "new_visitor",
             "users",
             "sessions",
             "bounces",
             "page_views",
             "engaged_users",
             "purchase_stage_user",
             "content_download",
             "partner_signup",
             "smb_signup",
             "smb_buynow",
             "load_timestamp",
             "dgtloadtimestamp"]

    # Load CSV and insert into PostgreSQL
    for chunk in pd.read_csv(csv_file_path, header=None, names=column_names, chunksize=10000):
        chunk.to_sql('duplicated_test', engine, index=False, if_exists='append')
        print(f"Inserted a chunk of {len(chunk)} rows.")
if __name__ == "__main__":
    main()



sh-4.2$ more Dockerfile 
FROM python:3.9-slim

# Install AWS SDK
RUN pip install boto3 pandas  sqlalchemy psycopg2-binary

# Copy the processing script
COPY process_file.py /app/process_file.py

WORKDIR /app

# Command to run when the container starts
CMD ["python", "process_file.py"]

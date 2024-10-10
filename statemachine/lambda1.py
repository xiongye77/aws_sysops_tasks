# the lambda which be triggered by S3 file upload and start statemachine
import json
import boto3

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Extract bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Construct input for the state machine
    state_machine_input = {
        'bucket': bucket,
        'key': key
    }

    # Start the Step Functions state machine
    response = sfn_client.start_execution(
        stateMachineArn='arn:aws:states:us-east-1:582140066777:stateMachine:StateMachine-json-csv-parquet-redshift',
        input=json.dumps(state_machine_input)
    )
    print (response)
    return {
        'statusCode': 200,
        'body': json.dumps('State machine started successfully.')
    }

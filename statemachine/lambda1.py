import json
import boto3
import datetime


sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Extract bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    
    # Format the date in 'yyyy-mm-dd-hh24' format
    
    melbourne_offset = datetime.timedelta(hours=11)  # AEDT (Australian Eastern Daylight Time)

    # Convert UTC time to Melbourne local time
    melbourne_time = utc_now + melbourne_offset

    # Format the date and time in 'yyyy-mm-dd-hh24' format
    formatted_time = melbourne_time.strftime("%Y-%m-%d-%H")
    # Construct input for the state machine
    state_machine_input = {
        'bucket': bucket,
        'key': key,
        'partition': formatted_time
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

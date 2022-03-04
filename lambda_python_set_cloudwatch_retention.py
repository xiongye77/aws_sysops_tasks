import boto3
import datetime
import sys

def change_cloudwatch_retention():
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    #regions =['ap-southeast-2']
    for region in regions:
        print("Region:", region)
        client = boto3.client('logs', region_name=region)
    
        paginator = client.get_paginator('describe_log_groups')
        for page in paginator.paginate():
            for group in page['logGroups']:
            #print(group)
                retentionInDays=group.get('retentionInDays')
                if (not retentionInDays):
                    print ("retention is never expired for", group['logGroupName'])
                    print("we will change ",group['logGroupName'],"retention days never expired ",  "to 3")
                    response = client.put_retention_policy(
                        logGroupName=group['logGroupName'],
                        retentionInDays=3
                    )
                else :
                #print (retentionInDays)
                    if int(retentionInDays) > 3:
                        print("we will change ",group['logGroupName'],"retention days from", retentionInDays, "to 3")
                        response = client.put_retention_policy(
                        logGroupName=group['logGroupName'],
                        retentionInDays=3
                        )
                
            
def lambda_handler(event, context):
    
    change_cloudwatch_retention()



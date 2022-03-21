import boto3
import datetime
import sys
import traceback
import re
#def lambda_handler(event, context):
orig_stdout = sys.stdout
account_id = boto3.client('sts').get_caller_identity().get('Account')
f = open('EC2_disable_detailed_monitor_%s.txt' % account_id, 'w')
sys.stdout = f



ec2 = boto3.client('ec2')
regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
#regions = ["us-west-2"]
for region in regions:
    print("Region:", region)
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]
            }
        ]
    )
    
    for instance in instances:
        monitoring_state = instance.monitoring['State']
        if monitoring_state == 'enabled':
            instance.unmonitor()
            print(f' We disabled detailed instance monitor  - Instance ID: {instance.id}')


sys.stdout = orig_stdout
f.close()

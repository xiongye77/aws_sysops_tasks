import boto3
from datetime import datetime
import sys
import re
import traceback

account_id = boto3.client('sts').get_caller_identity().get('Account')
orig_stdout = sys.stdout
f = open('Delete_stopped_EC2_instances_%s.txt' % account_id, 'w')
sys.stdout = f

ec2 = boto3.client('ec2')
regions = [region['RegionName']
     for region in ec2.describe_regions()['Regions']]

for region in regions:
    print("Region:", region)
    client = boto3.client('ec2',region)
    response = client.describe_instances()
    for r in response["Reservations"]:
        status = r["Instances"][0]["State"]["Name"]
        if status == "stopped":
            try:
                if str(r["Instances"][0]['Tags']).upper().find('KEEP') == -1 :
                    try:
                        stopped_time = re.findall('.*\((.*)\)', r["Instances"][0]['StateTransitionReason'])[0].replace(' GMT', '')
                        #print ('Stopped time:', stopped_time)
                        a=datetime.fromisoformat(stopped_time).date()
                        b=datetime.now().date()
                        c = b-a
                        if c.days > 20:
                            print(f"EC2 Instance" ,r["Instances"][0]["InstanceId"] ,"has stopped about",  c.days, "days and it does not have KEEP tag,will terminate it")
                            client.terminate_instances(InstanceIds=r["Instances"][0]["InstanceId"].split())
                    except Exception:
                        #traceback.print_exception(*sys.exc_info())
                        print(f"EC2 Instance" ,r["Instances"][0]["InstanceId"] ,"does not have stopped time and it does not have KEEP tag,will terminate it")
                        client.terminate_instances(InstanceIds=r["Instances"][0]["InstanceId"].split())
                        continue
            except Exception:
                #traceback.print_exception(*sys.exc_info())
                
                print(f"EC2 Instance" ,r["Instances"][0]["InstanceId"], "in region" , region ,"does not have any tag cause some excpetion,check later")
                continue
sys.stdout = orig_stdout
f.close()

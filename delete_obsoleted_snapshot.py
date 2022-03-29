import boto3
import datetime
import sys
import re
#def lambda_handler(event, context):

account_id = boto3.client('sts').get_caller_identity().get('Account')
orig_stdout = sys.stdout
f = open('Delete_snapshot_%s.txt' % account_id, 'w')
sys.stdout = f


ec2 = boto3.client('ec2')
regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

for region in regions:
    print("Region:", region)
    ec2 = boto3.client('ec2', region_name=region)
    auxiliaryList = []    
    
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    all_instances_response = ec2.describe_instances()
    all_used_images = []
    for reserve in all_instances_response['Reservations']:
        for insta_info in reserve['Instances']:
            image_id = insta_info['ImageId']
            if image_id not in all_used_images:
                all_used_images.append(insta_info['ImageId'])
        # Sort snapshots by date ascending
    #snapshots.sort()

    for snapshot in snapshots:
        a= snapshot['StartTime']
        b=a.date()
        c=datetime.datetime.now().date()
        d=c-b
        try:
            if d.days>14:
                id = snapshot['SnapshotId']
                print("Deleting snapshot:" ,id ,"because it is " ,d.days ," days old" )
                ec2.delete_snapshot(SnapshotId=id)
        except boto3.exceptions.botocore.client.ClientError as e:
            err_message = e.response["Error"]["Message"].strip("\"")
            print(err_message)
            ami_id = re.search( 'ami-[a-z0-9]+', err_message).group()

            if ami_id not in auxiliaryList:
                    auxiliaryList.append(ami_id)
            continue
    
    unused_list = list(set(auxiliaryList) - set(all_used_images))
    print("After compare following AMIs are needed by any EC2 instances")
    print(all_used_images)
    print("After compare following AMIs are not needed by any EC2 instances")  
    print(unused_list)
    
    for x in range(len(unused_list)):
        print(f"We will deregister_image",unused_list[x])
        
        ec2.deregister_image(ImageId=unused_list[x])
    
    print("After deregister_images delete snapshot again")
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    for snapshot in snapshots:
        a= snapshot['StartTime']
        b=a.date()
        c=datetime.datetime.now().date()
        d=c-b
        try:
            if d.days>14:
                id = snapshot['SnapshotId']
                print("Deleting snapshot:" ,id ,"because it is " ,d.days ," days old" )
                ec2.delete_snapshot(SnapshotId=id)
        except boto3.exceptions.botocore.client.ClientError as e:
            err_message = e.response["Error"]["Message"].strip("\"")
            print(err_message)
            



sys.stdout = orig_stdout
f.close()

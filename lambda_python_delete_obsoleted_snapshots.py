import boto3
import datetime
import sys
import traceback
import re
#def lambda_handler(event, context):
orig_stdout = sys.stdout
f = open('EBS_snapshot_delete.txt', 'w')
sys.stdout = f


account_id = boto3.client('sts').get_caller_identity().get('Account')
ec2 = boto3.client('ec2')
regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
#regions = ["us-west-2"]
for region in regions:
    print("Region:", region)
    ec2 = boto3.client('ec2', region_name=region)
        
    #response = ec2.describe_snapshots(Filters=[ { 'Name': 'description','Values':['db1-qa123-snapshot']}])
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    all_instances_response = ec2.describe_instances()
    #print (all_instances_response)
    auxiliaryList = []
    all_used_images = []
    for reserve in all_instances_response['Reservations']:
        for insta_info in reserve['Instances']:
            image_id = insta_info['ImageId']
            if image_id not in all_used_images:
                all_used_images.append(insta_info['ImageId'])
    print("We have following AMI used by EC2 instances")
    print (all_used_images)
    # Sort snapshots by date ascending
    #snapshots.sort()

    for snapshot in snapshots:
        a= snapshot['StartTime']
        b=a.date()
        c=datetime.datetime.now().date()
        d=c-b
        try:
            if d.days>10:
                id = snapshot['SnapshotId']
                description = snapshot['Description']

                searchObj = re.search( r'(.*) for (.*?) .*', description, re.M|re.I)
                ami_id = searchObj.group(2)
                if ami_id not in auxiliaryList:
                    auxiliaryList.append(ami_id)
                
                print("We should delete snapshot:" ,id ,"because it is " ,d.days ," days old", " and its volume size is ", snapshot['VolumeSize'],"GiB", " and its AMI is",ami_id  )
               
                #ec2.delete_snapshot(SnapshotId=id)
                print("We have deleted snapshot with snapshotid ",id)
        except Exception:
            traceback.print_exception(*sys.exc_info())
            continue
    print("We have following AMIs still needed by snapshots that could not be deleted ")    
    print (auxiliaryList)
    unused_list = list(set(auxiliaryList) - set(all_used_images))
    
    print("After compare following AMIs are not needed by any EC2 instances")  
    print (unused_list)

    for unused_list_image in unused_list:
        response = ec2.describe_images(ImageIds=[unused_list_image])
        print (response['Images'][0]['ImageId'],response['Images'][0]['ImageLocation'], response['Images'][0]['CreationDate'],response['Images'][0]['Description'])
    print  (len(auxiliaryList))
    print (len(unused_list))
    print("After compare following AMIs are still  needed by  EC2 instances") 
    print (list(set(auxiliaryList)-set(unused_list)))
sys.stdout = orig_stdout
f.close()

import boto3
import datetime




def delete_obsoleted_snapshot():
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    for region in regions:
        print("Region:", region)
        ec2 = boto3.client('ec2', region_name=region)
        
        #response = ec2.describe_snapshots(Filters=[ { 'Name': 'description','Values':['db1-qa123-snapshot']}])
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]

        # Sort snapshots by date ascending
        #snapshots.sort()

        for snapshot in snapshots:
            a= snapshot['StartTime']
            b=a.date()
            c=datetime.datetime.now().date()
            d=c-b
            try:
                if d.days>15:
                    id = snapshot['SnapshotId']
                
                    print("We should delete snapshot:" ,id ,"because it is " ,d.days ," days old", " and its volume size is ", snapshot['VolumeSize'],"GiB"  )
                    #client.delete_snapshot(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print ("skipping this snapshot")
                continue

def lambda_handler(event, context):
    
    delete_obsoleted_snapshot()

import boto3
import sys


orig_stdout = sys.stdout

ec2 = boto3.client('ec2')

account_id = boto3.client('sts').get_caller_identity().get('Account')
f = open('EBS_GP2_to_GP3_%s.txt' % account_id, 'w')
sys.stdout = f

regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

for region in regions:
    print("Region:", region)
	# Set the EC2 client
    ec2c = boto3.client("ec2", region_name=region)
 
    descvol = ec2c.describe_volumes(Filters=[{"Name": "volume-type", "Values": ["gp2"]}])
    gp2list = []

    for vol in descvol["Volumes"]:
        print("GP2 EBS volume found = {VolumeId}".format(**vol))
        gp2list.append(vol["VolumeId"])
    
    try:
        for vol in gp2list:
            ec2c.modify_volume(VolumeId=vol, VolumeType="gp3")
            print(f"GP2 EBS Vol modified to GP3: {vol}")
    except boto3.exceptions.botocore.client.ClientError as e:
        print(e.response["Error"]["Message"].strip("\""))
        continue



sys.stdout = orig_stdout
f.close()

# List the gp2 volumes in the account





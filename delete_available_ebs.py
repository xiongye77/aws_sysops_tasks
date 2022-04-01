import boto3
import datetime
import sys

orig_stdout = sys.stdout
account_id = boto3.client('sts').get_caller_identity().get('Account')
f = open('EBS_available_delete_%s.txt' % account_id, 'w')
sys.stdout = f

#def lambda_handler(object, context):

# Get list of regions
ec2_client = boto3.client('ec2')

regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    print("Region:", region)

        # List only unattached volumes ('available' vs. 'in-use')
    volumes = ec2.volumes.filter(
            Filters=[{'Name': 'status', 'Values': ['available']}])

    for volume in volumes:
       
        v = ec2.Volume(volume.id)
        try:
            for tag in v.tags:
                if tag['Key'].upper() == 'KEEP':
                    name = tag.get('Value')
                    print(name)
                    if name.upper() != 'TRUE':    
                        a= v.create_time
                        b=a.date()
                        c=datetime.datetime.now().date()
                        d=c-b
                        if d.days>10:
                            print("Volume",v.id ," is available and does not have keep tag on it or keep tag is false,so we will delete it")
                            print("Deleting EBS volume: {}, volume-type: {} Size: {} GiB Creation date {} ".format(v.id, v.volume_type ,v.size,v.create_time.strftime("%Y-%m-%d %H:%M:%S")))
                            v.delete()
        except Exception:
        # EBS volumes do not have any tags   
            a= v.create_time
            b=a.date()
            c=datetime.datetime.now().date()
            d=c-b
            if d.days>10:
                print("Volume",v.id ," is available and does not have any tag on it,so we will delete it")
                print("Deleting EBS volume: {}, volume-type: {} Size: {} GiB Creation date {} ".format(v.id, v.volume_type ,v.size,v.create_time.strftime("%Y-%m-%d %H:%M:%S")))
                v.delete()
            continue

sys.stdout = orig_stdout
f.close()

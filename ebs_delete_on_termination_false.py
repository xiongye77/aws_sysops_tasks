import boto3
import sys

account_id = boto3.client('sts').get_caller_identity().get('Account')
orig_stdout = sys.stdout
f = open('EBS_delete_on_termination_false_%s.txt' % account_id, 'w')
sys.stdout = f

ec2 = boto3.client('ec2')
regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
for region in regions:
    print("Region:", region)
    ec2 = boto3.client('ec2', region_name=region)
 
    asg_client = boto3.client('autoscaling',region_name=region)
    ec2_instance_id_list=[]
                    
    volumes = ec2.describe_volumes(Filters=[{"Name":"attachment.delete-on-termination", "Values":["false"]}])
    for volume in volumes["Volumes"]:
        if  volume.get('State')=='in-use':
            ec2_instance_id_list.append(volume["Attachments"][0].get('InstanceId'))
            print(volume["VolumeId"],volume["AvailabilityZone"],volume["State"], volume["Size"], volume["Attachments"][0].get('InstanceId'),volume["VolumeType"], volume["Attachments"][0].get('Device'))
            #print ('\n'.join(ec2_instance_id_list))

    unique_ec2_id_list=set(ec2_instance_id_list)
   
    asg_response = asg_client.describe_auto_scaling_groups()

    for i in asg_response['AutoScalingGroups']:
        for k in i['Instances']:
            if k['InstanceId'] in unique_ec2_id_list:
                unique_ec2_id_list.remove(k['InstanceId'])
                print ("We found instance ",k['InstanceId'], "in ASG group" ,i['AutoScalingGroupName'] ,"has EBS volume delete on termination false" )
    
    for instanceid in unique_ec2_id_list:
        print("We found instance",instanceid,"has EBS volume delete on termination false, it is not in any ASG")

sys.stdout = orig_stdout
f.close()


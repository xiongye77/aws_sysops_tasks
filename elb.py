# get all legacy ELB which without healthy or active targets, those ones can be safely removed, in my script, it will record load balancer configuration by running command describe_load_balancers 
import boto3
import pprint
import sys
import os
orig_stdout = sys.stdout

account_id = boto3.client('sts').get_caller_identity().get('Account')

f = open('ELB_info_%s.txt' % account_id, 'w')
sys.stdout = f


ec2 = boto3.client('ec2')

def getinstancename(instanceid):
        instances=ec2.describe_instances(Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                    instanceid
                ]
            },
        ],)
        resultset = {}    
        for instance in instances["Reservations"]:
            for inst in instance["Instances"]:
                resultset["State"]=inst["State"]["Name"]    
                for tag in inst["Tags"]:
                    if tag['Key'] == 'Name':
                        resultset["Name"]=tag['Value']
      
        return resultset
             
def getinstancehealth(lbname,instanceid):
    instancestate=elb.describe_instance_health(
                LoadBalancerName=lbname,
                Instances = [{
                    'InstanceId' : instanceid
                }]
        )
    return instancestate['InstanceStates'][0]['State']

regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
for region in regions:
    print("Region:", region)
    elb = boto3.client('elb',region)
    unused_lb=[]
    all_lb_name=[]
    healthy_lb=[]
    lbs = elb.describe_load_balancers(PageSize=400)
    for lb in lbs["LoadBalancerDescriptions"]:
        #print("\n"*2)
        #print ("-"*6)
        #print("Name:",lb["LoadBalancerName"])
        #print("HealthCheck:",lb["HealthCheck"])
        #print("Instance Info:")
        all_lb_name.append(lb["LoadBalancerName"])
        if len(lb["Instances"]) == 0:
            print("Load balancer:",lb["LoadBalancerName"],"does not have Instance is mapped")
            unused_lb.append(lb["LoadBalancerName"])
            lb_name=lb["LoadBalancerName"]
            #elb_info=os.system("aws elb describe-load-balancers --load-balancer-name {}".format(lb_name))
            #print(elb_info)
            response=elb.describe_load_balancers(LoadBalancerNames=[lb_name])
            print(response)
        for instance in lb["Instances"]:
            #instance.update(getinstancename(instance["InstanceId"]))
            instance['Health']=getinstancehealth(lb["LoadBalancerName"], instance["InstanceId"])
            if instance['Health'] =='InService':
                healthy_lb.append(lb["LoadBalancerName"])
    #  get a list of ELB without healthy target print(list(set(all_lb_name)-set(healthy_lb)-set(unused_lb)))
    for lb_name in  list(set(all_lb_name)-set(healthy_lb)-set(unused_lb)):
        print ("Load balancer" ,lb_name ,"does not have health target.")
        response=elb.describe_load_balancers(LoadBalancerNames=[lb_name])
        print(response)


sys.stdout = orig_stdout
f.close()

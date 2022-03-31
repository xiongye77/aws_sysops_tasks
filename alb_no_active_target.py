import boto3
import pprint
import sys

orig_stdout = sys.stdout

account_id = boto3.client('sts').get_caller_identity().get('Account')

f = open('ALB_info_%s.txt' % account_id, 'w')
sys.stdout = f


def gettargetgroups(arn):
    tgs=elb.describe_target_groups(LoadBalancerArn=arn)
    tgstring=[]
    for tg in tgs["TargetGroups"]:
        tgstring.append(tg["TargetGroupName"])
    return tgstring
def gettargetgrouparns(arn):
    tgs=elb.describe_target_groups(LoadBalancerArn=arn)
    tgarns=[]
    for tg in tgs["TargetGroups"]:
        tgarns.append(tg["TargetGroupArn"])
    return tgarns
def getinstancename(instanceid):
    instances=ec2.describe_instances(Filters=[
        {
            'Name': 'instance-id',
            'Values': [
                instanceid
            ]
        },
    ],)
    for instance in instances["Reservations"]:
        for inst in instance["Instances"]:
            #print(type(inst["Tags"]))
            try:
                for tag in inst["Tags"]:
                    if tag['Key'] == 'Name':
                        return (tag['Value'])
            except Exception:
                
                print ("Instance", inst["InstanceId"],"does not have any tag")
                continue
def gettargethealth(arn,lbname):
    inss=elb.describe_target_health(TargetGroupArn=arn)
    #print(len(inss))
    #print(inss)
    instanceids=[]
    #print(len(inss["TargetHealthDescriptions"]))
    if len(inss["TargetHealthDescriptions"]) == 0:
        print("LB",lbname,"does not have active backend instances")
    for ins in inss["TargetHealthDescriptions"]:
        ins["Name"]=getinstancename(ins['Target']['Id'])
        #nstanceids.append(ins['Target']['Id'])
        print (ins)
        
    

ec2 = boto3.client('ec2')


regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
for region in regions:
    print("Region",region)
    elb = boto3.client('elbv2',region)
    lbs = elb.describe_load_balancers(PageSize=400)
    unused_lb_list=[]
    no_healthy_target=[]
    for lb in lbs["LoadBalancers"]:
        print("\n"*2)
        print ("-"*6)
        print("Name:",lb["LoadBalancerName"])
        print("Type:",lb["Type"])
        print("TargetGroups:",str(gettargetgroups(lb["LoadBalancerArn"])))
        #print(gettargetgrouparns(lb["LoadBalancerArn"]))           
        for tgs in gettargetgrouparns(lb["LoadBalancerArn"]):
            target_health_status=[]
            inss=elb.describe_target_health(TargetGroupArn=tgs)
            if len(inss["TargetHealthDescriptions"]) == 0:
                unused_lb_list.append(lb["LoadBalancerName"])
            for ins in inss["TargetHealthDescriptions"]:
                
                ins["Name"]=getinstancename(ins['Target']['Id'])
                #nstanceids.append(ins['Target']['Id'])
                print (ins)
                target_health_status.append(ins["TargetHealth"]["State"])

            if 'healthy' not in  target_health_status:
                no_healthy_target.append(lb["LoadBalancerName"])   

            #gettargethealth(tgs,lb["LoadBalancerName"])
    print("\n"*4)
    print("Region" , region, "Account id", account_id, "no active and no health target ALB information summary as following ")
    
    print ("-"*12)
    for lb_name in  unused_lb_list:
        print ("Load balancer" ,lb_name ,"does not have active target.")
    
    print("\n"*1)
    print ("-"*12)

    for lb_name in list(set(no_healthy_target)-set(unused_lb_list)):
        print ("Load balancer" ,lb_name ,"does not have health target.")
    
    print("\n"*4)
sys.stdout = orig_stdout
f.close()

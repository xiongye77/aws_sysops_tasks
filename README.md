# AWS cost optimization 

AWS Cost explorer verify which service cost mostly

found cloudwatch cost 3000$ per month. 

should  keep application logging level optimized as per need. Don’t create unnecessary logs/For AWS provided resources, enable only required amount of logging (for example, RDS provides 3–4 various categories of logs. In Development environment, none of them is being used)/VPC logs, Flow logs should be configured carefully (should be enabled only for those where it is required)/Log-Retention Period: Many AWS services directly creates log-groups and starts logging. These kinds of log-groups keep storing more and more data without archiving.

![image](https://user-images.githubusercontent.com/36766101/156666941-ba03bf80-0919-4a0c-a82d-e7ad11058a97.png)


Use eventbridge to trigger lambda function to delete all EBS volumes in available status and do not have related tags.  

![image](https://user-images.githubusercontent.com/36766101/156667805-3749ab7a-e497-47e1-97cd-6362c2ead6d3.png)


Use eventbridge to trigger lambda function to delete all snapshots longer than 15 days and do not have related tags.  

https://github.com/xiongye77/aws_sysops_tasks/blob/main/lambda_python_delete_obsoleted_snapshots.py

Change EBS snapshot lifecycle to sensible days

![image](https://user-images.githubusercontent.com/36766101/156670238-9504a73c-cc05-4ff6-a090-92ea566afddf.png)


aws_rds_tasks

Purchase reserved DB instances


Take snapshot from RDS DB and choose snapshot to migrate to Aurora 

![image](https://user-images.githubusercontent.com/36766101/156263093-fd91db24-95bc-441c-b3a9-4fa2731f049f.png)


Add read replica for Aurora 
![image](https://user-images.githubusercontent.com/36766101/156267895-7ad8c3ec-7559-45a6-935c-9a208f6a638e.png)




DMS migration for on-prem to RDS 

![image](https://user-images.githubusercontent.com/36766101/156293396-64ba714b-5039-4b0b-8fde-433e66a853bd.png)


WAF block traffic based on rules.

![image](https://user-images.githubusercontent.com/36766101/156465746-e23c285c-0ea5-4e2c-a884-c16e28ddeda1.png)
![image](https://user-images.githubusercontent.com/36766101/156465979-f9948126-98d6-461f-80bb-0b15a132e456.png)



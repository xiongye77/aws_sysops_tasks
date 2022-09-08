# AWS cost optimization 

Trust advisor suggestions check. 

![image](https://user-images.githubusercontent.com/36766101/165426657-889af21a-f9f4-4e29-a3cf-d773a4d58589.png)


Adjust EC2 instance size not only based on cpu usage, but also based on memory usage, some EC2 instances cpu usage is low ,but memory usage is high.
Use SSM run command with powershell to install cloudwatch agent on Windows and Ansible to install cloudwatch agent on Linux.Load cloudwatch agent configuration file from S3. 

https://github.com/xiongye77/aws_sysops_tasks/blob/main/install_load_cloudwatch_agent


Check ALB if they have active target instances. Sometimes ALB does not have healthy targets and even no targets, those can be safely dropped. 
https://github.com/xiongye77/aws_sysops_tasks/blob/main/alb_no_active_target.py




Deploy and enable Cost Anomaly Alerts to your AWS organization payer account.Make sure you have slack channel prepared as parameter for 
defaultSlackWebhookURL	https://hooks.slack.com/services/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   
https://github.com/ighanim/aws-cost-anomaly-alerts

![image](https://user-images.githubusercontent.com/36766101/159828197-6f239317-6af7-46c5-ad9f-ffd2cdf7f8ca.png)
![image](https://user-images.githubusercontent.com/36766101/159828368-566f4a80-45f1-4fd8-834b-b3a0bf0b0745.png)
![image](https://user-images.githubusercontent.com/36766101/159828396-eea4787d-31e2-425b-bd1f-417db0ac1154.png)



Disable EC2 instance detailed monitor since we have new relic for performance and Sumologic for log analyze.
https://github.com/xiongye77/aws_sysops_tasks/blob/main/disable_ec2_detailed_monitor.py



![image](https://user-images.githubusercontent.com/36766101/171834736-df29e1c9-eb9a-431d-be3c-1b861f1f7615.png)
20222/06/03 Found one account NatGateway-Bytes cost spiked from 1 thousand to 11 thousands.
Check VPC flow logs use query based on 
https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html
https://aws.amazon.com/premiumsupport/knowledge-center/vpc-find-traffic-sources-nat-gateway/

![image](https://user-images.githubusercontent.com/36766101/171835267-374df62c-b627-4fba-8b57-8250e263276c.png)
Those source IPs belong to AWS cloudfront IPs (https://ip-ranges.amazonaws.com/ip-ranges.json), so guess lots of downloa traffic in private subnets from cloudfront. 

Use Session Manager login EC2 instance and install iftop to monitor network traffic 
![image](https://user-images.githubusercontent.com/36766101/171994335-e77b187b-2924-4c74-a309-e64fb8e0774f.png)


AWS Cost explorer verify which service cost mostly

found cloudwatch cost 3000$ per month. 

should  keep application logging level optimized as per need. Don’t create unnecessary logs/For AWS provided resources, enable only required amount of logging (for example, RDS provides 3–4 various categories of logs. In Development environment, none of them is being used)/VPC logs, Flow logs should be configured carefully (should be enabled only for those where it is required)/Log-Retention Period: Many AWS services directly creates log-groups and starts logging. These kinds of log-groups keep storing more and more data without archiving.

![image](https://user-images.githubusercontent.com/36766101/156666941-ba03bf80-0919-4a0c-a82d-e7ad11058a97.png)


Use eventbridge to trigger lambda function to delete all EBS volumes in available status and do not have related tags.  

![image](https://user-images.githubusercontent.com/36766101/156667805-3749ab7a-e497-47e1-97cd-6362c2ead6d3.png)


Use eventbridge to trigger lambda function to delete all snapshots longer than 15 days and do not have related tags.  

https://github.com/xiongye77/aws_sysops_tasks/blob/main/lambda_python_delete_obsoleted_snapshots.py


Use eventbridge to trigger lambda function to set cloudwatch log group retention to 3 days

https://github.com/xiongye77/aws_sysops_tasks/blob/main/lambda_python_set_cloudwatch_retention.py

Change EBS snapshot lifecycle to sensible days

![image](https://user-images.githubusercontent.com/36766101/156670238-9504a73c-cc05-4ff6-a090-92ea566afddf.png)


# AWS_RDS_tasks
RDS Architecture
![image](https://user-images.githubusercontent.com/36766101/159101346-984f200f-1798-4d6c-8efb-e280a9ff283d.png)


RDS will automatically perform minor verion upgrade if option is enabled, even if Multi-AZ enabled, it will still cause downtime (Downtime is within designated maintenance window). Another option is choose dedicated maintenance window to perform minor/major upgrade directly. 

![image](https://user-images.githubusercontent.com/36766101/159425050-3a65d722-77e6-44ee-a54f-1c56c13f4dff.png)


Check production AWS RDS backup automatically backup is enabled and configure cross region replication if needed (Also check RDS has proper maintenance windows and backup window.)/Delete old RDS snapshots 

![image](https://user-images.githubusercontent.com/36766101/159447132-3df36689-56f4-496d-a7d2-472caf8634df.png)




Purchase reserved DB instances


Take snapshot from RDS DB and choose snapshot to migrate to Aurora 

![image](https://user-images.githubusercontent.com/36766101/156263093-fd91db24-95bc-441c-b3a9-4fa2731f049f.png)


Add read replica for Aurora 
![image](https://user-images.githubusercontent.com/36766101/156267895-7ad8c3ec-7559-45a6-935c-9a208f6a638e.png)




DMS migration for on-prem to RDS 

![image](https://user-images.githubusercontent.com/36766101/156293396-64ba714b-5039-4b0b-8fde-433e66a853bd.png)



RDS migrate to Aurora (Due to read replica count limitation)

Stop all DB writing applications/batch jobs
Create the RDS Snapshot
Create Aurora cluster from the RDS snapshot
Create Aurora instances
Upgrade the Aurora cluster from 9.6.11 to 10.11
Upgrade the Aurora cluster from 10.11 to 11.8
Test new cluster
Add regional clusters
Connect test applications to the new DB clusters
Application test
Switch production applications to the new DB clusters
Resume DB writing applications/batch jobs


# AWS shield protect against layer 3 or layer 4 attacktion and WAF protect against layer 7
Sheild protect against SYN/UDP floods, reflection attacks ,DDos attacks.
WAF protect against sql injection/cross site scripting/Block specific IPs or Countries. 

# WAF block traffic based on rules.

![image](https://user-images.githubusercontent.com/36766101/156465746-e23c285c-0ea5-4e2c-a884-c16e28ddeda1.png)
![image](https://user-images.githubusercontent.com/36766101/156465979-f9948126-98d6-461f-80bb-0b15a132e456.png)

# Cross account cloudtrail gather to one dedicated S3 bucket under security review account 

![image](https://user-images.githubusercontent.com/36766101/159195015-f08b19f9-d6ef-472e-bc2e-a6795f1a0b3c.png)
![image](https://user-images.githubusercontent.com/36766101/159195104-66626a0d-9cd7-41c1-b348-bb906441930f.png)



# cloudfront access log check 
Cloudfront connect to origin web site always report 502 error, check cloudfront log use Athena. After check AWS document, it related to Cloudfront could not connect to origin. 
To fix this error, either have to change origin protocol policy from HTTPS to HTTP such that CloudFront does not use HTTPS while trying to connect to the origin rather uses HTTP. Alternatively, work with the origin to make sure that when CloudFront makes a request to the origin with SNI value of "aepcdp.carsales.com.au" it should respond with a certificate that either covers the origin domain name or the host header value that you will be forwarding.

Since we need ensure security in transit, so we have to work with Adobe on accept cloudfront https connection. 


the Viewer protocol policy still https only -> Viewer protocol policy determines the connection between the client/browser and CloudFront so that should not impact the website

![image](https://user-images.githubusercontent.com/36766101/157428045-9ba3dd09-7f93-49c9-85bd-6355afaf48a5.png)
![image](https://user-images.githubusercontent.com/36766101/157428243-2141416f-bcb7-4883-a48e-edb5b8034c8e.png)


Control origin request (When a viewer request to CloudFront results in a cache miss (the requested object is not cached at the edge location), CloudFront sends a request to the origin to retrieve the object. This is called an origin request)
Some information from the viewer request, such as URL query strings, HTTP headers, and cookies, is not included in the origin request by default. But you might want to receive some of this other information at the origin, for example to collect data for analytics or telemetry. You can use an origin request policy to control the information that’s included in an origin request.

![image](https://user-images.githubusercontent.com/36766101/157431965-b7544cd5-374f-486c-a7cf-663f09d4d675.png)



# Bucket policy to control IP access bucket 
Command to verify the ACL information of a specific object:

aws s3api get-object-acl --bucket bucket_name --key filename.txt

Command to upload object with specific ACL
aws s3 cp filename.txt s3://bucket_name/ --acl bucket-owner-full-control

![image](https://user-images.githubusercontent.com/36766101/158493350-385d1170-75ae-4e05-a495-e3748621e9da.png)


# AWS config managed rule for S3 
![image](https://user-images.githubusercontent.com/36766101/158534351-48507195-fa34-42f1-9c88-ba36c974ac29.png)

s3-bucket-public-read-prohibited
s3-bucket-public-read-prohibited
s3-bucket-server-side-encryption-enabled
s3-bucket-versioning-enabled


# AWS S3 Increasing S3 Transfer Speeds with Transfer Acceleration
Use Cloudfront edge location to accelerate S3 upload performance , create dedicated upload endpoint which incur an additional fee.
Enhancing S3 Performance with Multipart Upload.This feature lets a service breaks a big file into smaller chunks and then uploads them; once all parts are uploaded, S3 could merge all in one single file. By doing this, you could also benefit from multithreading and start uploading many chunks simultaneously


# Redshift access audit 
Queries that are run are logged in STL_QUERY. DDL statements are logged in STL_DDLTEXT. 
![image](https://user-images.githubusercontent.com/36766101/163095697-ea3c8684-1946-4029-9679-1df82e8b9091.png)
![image](https://user-images.githubusercontent.com/36766101/163095746-f8e212d6-7ed0-448b-ade9-dd0eb72b9b75.png)

For the user activity log, you must also enable the enable_user_activity_logging database parameter. If you enable only the audit logging feature, but not the associated parameter, the database audit logs log information for only the connection log and user log, but not for the user activity log. 

For connection log, use AWS Glue to run crawler to S3 bucket and Use Athena to check the result
![image](https://user-images.githubusercontent.com/36766101/163096475-03c64669-bade-4b5b-ad15-6680ed3a1e8c.png)


# AWS Security hub and GuardDuty integration 

![image](https://user-images.githubusercontent.com/36766101/163169127-cbfdc4cc-9dec-48d8-8c39-d0f899e48ecd.png)
![image](https://user-images.githubusercontent.com/36766101/163169541-0714e3f4-4146-4d57-9947-34f7488b4f25.png)

# AWS S3 presigned url for temporary access of private contents.
We have one Windows bastion host could not use sftp to send fileout and could not use aws s3 cp command to send fileout due to IAM role limitation,but it can use internet, so we use S3 presigned url to allow it post file to S3.One python code running on EC2 will IAM role to generate presigned url and python program on Windows bastion host will wget it and post file 

https://github.com/xiongye77/aws_sysops_tasks/blob/main/s3_presigned_url.py



# AWS CloudWatch Synthetics to monitor Jenkins
We can use AWS CloudWatch Synthetics to monitor Jenkins master(10.240.10.35) server health status, if this page could not be loaded, we will use cloudwatch event bridge to reboot the Jenkins master 

 ![image](https://user-images.githubusercontent.com/36766101/178485174-eacb5a56-4217-47fc-af50-02a502c887d3.png)


Based on document How do I monitor the performance of my website using CloudWatch Synthetics? (amazon.com) (https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-synthetics-performance/)  We create jenkins-monitor and use command aws synthetics  describe-canaries --name jenkins-monitor  to get its id. 

During the configuration, just make sure we set 

VPC/Subnet/Security Group information same as the Jenkins master server 
The url check information to internal IP of the EC2 instance instead of Carsales internal Jenkins url or the lambda function could not reach target Jenkins master
Schedule is Run continuously change to 5 minutes make sure there is enough time for application can accept request after EC2 instance reboot. 

After setup, the Synthetics Canaries  configuration as  CloudWatch Management Console (amazon.com)  and monitor tab as following 


Next step is create event bridge to response if the Synthetics Canaries check failed. 




Create event pattern as following the  canary-id is get from aws synthetics  describe-canaries --name jenkins-monitor
{
  "source": ["aws.synthetics"],
  "detail-type": ["Synthetics Canary TestRun Failure"],
  "region": ["ap-southeast-2"],
  "detail": {
    "account-id": ["153576335202"],
    "canary-id": ["e6f642ad-aa07-4699-93e2-3f9bdd77ff02"],
    "canary-name": ["jenkins-monitor"]
  }
} 

The targets of EventBridge  will be EC2 instance reboot, the input Constant id EC2 instance id


![image](https://user-images.githubusercontent.com/36766101/178484626-96924d58-8706-4fc7-b6f5-0924419320a5.png)
 


# Optional configuration

Synthetics Canaries jenkins-monitor  has one cloudwatch alarm, we can configure SNS Topics to send email alarm once it triggered.





# Creating the table for CloudTrail logs in Athena using partition projection

![image](https://user-images.githubusercontent.com/36766101/187150154-68efa3ae-f156-4054-ba4e-a83c1b4e363a.png)

https://aws.amazon.com/premiumsupport/knowledge-center/athena-tables-search-cloudtrail-logs/
https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html#create-cloudtrail-table-partition-projection
https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html


# AWS Secret Manager use KMS key for encryption
Secrets Manager uses the KMS key that is associated with a secret to generate a data key for each secret value. Secrets Manager also uses the KMS key to decrypt that data key when it needs to decrypt the encrypted secret value. 

If you don't specify an KMS encryption key, Secrets Manager uses the Amazon Web Services managed key aws/secretsmanager .




 aws secretsmanager create-secret     --name MyTestSecret     --description "My test secret created with the CLI."     --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}" --region  ap-southeast-2  --kms-key-id arn:aws:kms:ap-southeast-2:333186395126:key/c89492e9-088a-4e09-b9bd-3515064fe6a3
 aws secretsmanager update-secret --region ap-southeast-2 --secret-id key --kms-key-id arn:aws:kms:ap-southeast-2:333186395126:key/c89492e9-088a-4e09-b9bd-3515064fe6a3
 
![image](https://user-images.githubusercontent.com/36766101/187192234-3c599927-e7ca-4077-afd1-130a090d7302.png)
![image](https://user-images.githubusercontent.com/36766101/187194004-bba08e43-a86f-432e-ae1f-759cc186355d.png)



# AWS Dynamodb export table to S3 and use Glue/Athena to query data use SQL
https://aws.amazon.com/blogs/database/export-and-analyze-amazon-dynamodb-data-in-an-amazon-s3-data-lake-in-apache-parquet-format/
![image](https://user-images.githubusercontent.com/36766101/188264197-c0157a69-fba4-405d-b465-62ca2395a244.png)

Step 1 Export Dynamodb table data to S3
![image](https://user-images.githubusercontent.com/36766101/188264343-a37ffc8d-7e0d-420d-9944-2551de0244d2.png)

Step2 Run Glue crawler on the exported S3 folder to get table created
![image](https://user-images.githubusercontent.com/36766101/188264390-fc3d4998-8cac-4347-8639-9686f2893455.png)

Step 3 Athena query table using SQL which could not run Dynamodb directly
![image](https://user-images.githubusercontent.com/36766101/188264528-31fa841b-6ac5-49b2-b6e4-df38e985888e.png)



# Utilize AWS RDS proxy when using lambda to connect RDS database
https://github.com/xiongye77/aws_sysops_tasks/blob/main/rds.yml
https://github.com/xiongye77/aws_sysops_tasks/blob/main/rds_proxy.yml
![image](https://user-images.githubusercontent.com/36766101/188251264-b2668b35-be80-489e-93a3-14c637ef6d58.png)
RDS Proxy is a solution provided by AWS to manage database connections in a serverless architecture environment.In our problem, a large number of database connections will be created based on the number of Lambda functions invoked. RDS proxy solves this problem by sharing the database connections. Following is the flow when we configure the RDS proxy with our Lambda functions.

Lambda will call the RDS proxy, not the RDS instance directly to get a database connection.

Based on the availability of the connection pool, a connection will be returned back to our Lambda function.

Lambda function will use this connection to connect to the database.

Once function invocation is done this connection will be removed and returned back to connection pool.


# AWS Service Catalog
![image](https://user-images.githubusercontent.com/36766101/189024965-44ebe02d-49e5-48c9-ae59-062a7dae771e.png)

# AWS layer 7 firewall
![image](https://user-images.githubusercontent.com/36766101/189025758-3bbc2b83-3655-4f6a-9106-9321ea734e8a.png)
WAF
![image](https://user-images.githubusercontent.com/36766101/189032230-34589c04-a44c-49a3-8b92-a253a8a3481d.png)



![image](https://user-images.githubusercontent.com/36766101/189041237-e2b3932c-61d2-4642-a9af-ba5644dea635.png)

# AWS Sys Ops 

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

# AWS DevSecOps and related tool 2023/01/31
![image](https://user-images.githubusercontent.com/36766101/215660623-248f7429-e582-4ad5-ae8d-6e488a128a97.png)
![image](https://user-images.githubusercontent.com/36766101/215669934-b3005317-72d5-4bec-88b8-5aaa824b1a67.png)


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


# AWS Resource Access Manager 
![image](https://user-images.githubusercontent.com/36766101/189049207-1e37572f-fa48-489f-b052-fe80c3033c94.png)

![image](https://user-images.githubusercontent.com/36766101/189049255-c451eed4-9a69-4696-a99a-a07bcae13cf3.png)


# AWS layer 7 firewall
![image](https://user-images.githubusercontent.com/36766101/189025758-3bbc2b83-3655-4f6a-9106-9321ea734e8a.png)
WAF
![image](https://user-images.githubusercontent.com/36766101/189032230-34589c04-a44c-49a3-8b92-a253a8a3481d.png)



![image](https://user-images.githubusercontent.com/36766101/189041237-e2b3932c-61d2-4642-a9af-ba5644dea635.png)



# RDS Event retention to Cloudwatch
![image](https://user-images.githubusercontent.com/36766101/189503396-fcc06dd1-664e-4671-8e60-e8bf880b2dee.png)




# Cross account event send through EventBridge
![image](https://user-images.githubusercontent.com/36766101/190831177-1cf9bf25-fc13-4033-9687-58a6c3df76bb.png)
![image](https://user-images.githubusercontent.com/36766101/189504959-1553d0e8-a002-4e9b-b2da-79829ca2521b.png)
![image](https://user-images.githubusercontent.com/36766101/189504952-7121628b-31b2-4a76-a78a-fd2a7cb9ae7b.png)
![image](https://user-images.githubusercontent.com/36766101/190830363-f5b29e4a-7149-4d6b-9212-befd42dec71d.png)

By putting a resource policy in place on the SecOps Event Bus in the security account, the SecOps team can easily allow all accounts within the organization (or specific Organizational Units) to send events to the centralized event bus. They can then put a pattern match in place via a rule on the event bus that looks for specific events generated from within the organizational accounts that need to be reviewed and potentially addressed.

For this example above, we have a junior engineer who maliciously or accidentally deletes an Amazon Elastic Container Registry image from their development account. SecOps doesn’t want any junior engineers to be able to purge images; instead, they only want senior engineers to do so.

To identify issues like this, they share their Event Bus to the organization, create a resource policy allowing the organization to send events cross-account and cross-region, and then implement a rule on every child AWS account’s default event bus.

This default rule would be a pattern match for the DELETE action-type field in the incoming ECR events. Once it matches, it would send this event to the SecOps account event bus, which they can then handle however they see fit.

In this example, they simply use SNS to send an alert to their SecOps engineer team. However, we could integrate with a SaaS like PagerDuty to handle alerts and notifications as well.
![image](https://user-images.githubusercontent.com/36766101/189504829-eb55613f-979b-4b35-9448-191299c63b12.png)
![image](https://user-images.githubusercontent.com/36766101/189504837-0d5c9ba8-a9f8-46fb-88ed-b93dbb96aa37.png)





![image](https://user-images.githubusercontent.com/36766101/191006257-d5b3b828-6800-4ec9-a42f-a8b0c56c15d4.png)

A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

Amazon Cognito identity pools (federated identities) enable you to create unique identities for your users and federate them with identity providers. With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other AWS services. 

This lesson reviews the features of the product and talks through some example architectures.


# Stream AWS Cloudwatch Logs to Amazon OpenSearch Service (successor to Amazon Elasticsearch Service)

![image](https://user-images.githubusercontent.com/36766101/191262883-ebe59164-2ca9-4d85-aa15-43243bf7136c.png)



# AWS Eventbrige
four components:Event source,Event bus,Rule,Target
![image](https://user-images.githubusercontent.com/36766101/191629505-d38ffef7-fbb0-43ed-93f1-546a59c672a4.png)




# AWS Guardguty Cross account security check and send security finding to slack through cloudwatch event.
![image](https://user-images.githubusercontent.com/36766101/191954018-ef6a7f45-b2d1-4891-bc92-1bf041e9eac5.png)
![image](https://user-images.githubusercontent.com/36766101/191954490-eb6d077e-a8b3-4ea6-8207-1bdc36237612.png)


# Amazon Detective 
Amazon Detective is a service that helps you analyze and investigate the root cause of security findings or suspicious activity. Using data from AWS Cloudtrail logs, VPC flow logs and AWS GuardDuty data, Amazon Detective will collate, filter the collected security data and using AWS Security Hub, GuardDuty, integrated partner security products, machine learning and statistical analysis investigates the security findings to get to the root cause of the problem or suspicious activity.
![image](https://user-images.githubusercontent.com/36766101/192092102-217c98f8-f5fe-4356-94d2-857619c990cf.png)


# AWS ES for ingest log 
![image](https://user-images.githubusercontent.com/36766101/194179837-a1f03e07-f11c-4331-9306-39706c5e5f32.png)

You can configure a CloudWatch Logs log group to stream data it receives to your Amazon OpenSearch Service cluster in near real-time through a CloudWatch Logs subscription. 
![image](https://user-images.githubusercontent.com/36766101/194182897-2c95253f-98ca-46d6-90a3-a7157d3e69ac.png)
![image](https://user-images.githubusercontent.com/36766101/194193722-4c5fab31-df3c-4595-8c08-08cde519e6c5.png)


# AWS DMS migration task replication ongoing

![image](https://user-images.githubusercontent.com/36766101/194701168-15426c6d-0f6e-416a-9fbe-2247a5b273b4.png)


# Kafka VS AWS SNS + SQS (2022/10/14)
Apache Kafka, we have something called as consumer groups, where we can group our consumers into different groups and then start listening to the same topic. so all consumer groups subscribe same topic will get same message that send to same topic.Each Consumer Group will maintain its own set of offsets and receive messages independently from other consumer groups on the same topic. To say it simply, a message received by Consumer Group 1 will also be received by Consumer Group 2. Within a single consumer group, a consumer will not receive the same messages as other consumers in the same consumer group.
![image](https://user-images.githubusercontent.com/36766101/195725403-73a89185-5fa0-4dda-8f04-20531e83e98f.png)
![image](https://user-images.githubusercontent.com/36766101/195726963-4a3900f1-6f52-4983-8c74-4124bdf309e0.png)

For AWS , We will create three different SQS queues which subscribe to same SNS topic. What happens here is, whenever we write something to the SNS topic, a copy of that message or data is sent to each SQS queue that has subscribed to the SNS topic.
![image](https://user-images.githubusercontent.com/36766101/195725446-c630471b-7708-4574-843b-6609839a93f0.png)


# Security hub automaticaly send findings to SNS (2022/10/24)
![image](https://user-images.githubusercontent.com/36766101/197424822-a4bdce79-6fed-4aa3-8e20-c9c00ce7849d.png)


# GuardDuty findings and export to S3 use KMS key(2022/11/22)
![image](https://user-images.githubusercontent.com/36766101/203194553-4b657457-484b-4726-877a-be4b50b20538.png)
![image](https://user-images.githubusercontent.com/36766101/203194819-6ddada14-3e6e-49f5-96cc-f2e92d277e6b.png)
![image](https://user-images.githubusercontent.com/36766101/203194958-df648d6c-6401-4a3e-b07c-3225910e3755.png)


# Different 5xx errors and their corresponding means (2022/11/27)
![image](https://user-images.githubusercontent.com/36766101/204116449-d552b4f2-62ae-48af-a220-ea4163984dd3.png)

502 Bad Gateway
A 502 error means that a website server that is serving as a reverse proxy for the website origin server (for example, a CDN PoP) did not receive a valid response from the origin server. This may be because the origin server is experiencing issues, there is an invalid or incorrect DNS name, or because a firewall on the origin server has blocked the reverse proxy server request.

503 Service Unavailable
The 503 service unavailable message means that the website origin server is not available and is usually a temporary state. This error could be triggered because something running on the website server side has crashed or your site is purposefully down for maintenance. This error is also commonly served when a site has more traffic than it can handle.

504 Gateway Timeout
Similar to the 502 error, the 504 Gateway Timeout error occurs if the server that is acting as a proxy for the website origin server did not receive a response from the website origin server within a set time period. 

Troubleshooting 500 errors
502 and 504 errors are related to a bad gateway, meaning that while the reverse proxy server is operational, something it needs to collect from the origin server is not working, or the connection between the reverse proxy server and the origin server is broken. To troubleshoot this issue, websites should check that their origin server and all the servers it needs to access are running correctly, and then check the configuration between the origin server and reverse proxy server.

503 errors are often expected when your website is going through downtime in order to make updates or changes. They may also be triggered by a large influx of traffic to your website.


# Patch EC2 instances use SSM patch manager/SSM patch baseline/SSM document (2023/01/11)
https://github.com/xiongye77/ssm-patch-manager


# Implement this SAGA pattern flows with using AWS Step Function (2023/01/13)

![image](https://user-images.githubusercontent.com/36766101/215025585-7a967a8a-90e7-423f-b192-52357ed1e412.png)

We will use SAGA Orchestration to implement e-commerce place order use case for happy and failure states.

1 Create API Gateway to trigger to AWS Step functions when place-order request comes from customer

2 Saga orchestration pattern implementation with AWS Step Functions

3 Success & Failure paths in a distributed transactions

4 Restoring data consistency in Amazon DynamoDB database

![image](https://user-images.githubusercontent.com/36766101/212228168-804742ce-a6a0-40ce-8ddb-711f8cca356b.png)
![image](https://user-images.githubusercontent.com/36766101/212231331-c1baca90-f69d-4e3a-b494-8724ce705a38.png)

![image](https://user-images.githubusercontent.com/36766101/212238147-e9abedf7-66aa-4577-9729-17f0b8b827ed.png)

The saga pattern is a failure management pattern that helps establish consistency in distributed applications, and coordinates transactions between multiple microservices to maintain data consistency. A microservice publishes an event for every transaction, and the next transaction is initiated based on the event's outcome. It can take two different paths, depending on the success or failure of the transactions.

![image](https://user-images.githubusercontent.com/36766101/212242458-8a75f2c7-617c-40d5-ad49-7bc38c08da46.png)


# AWS eventbridge eventbus/event rule with pattern/targets

![image](https://user-images.githubusercontent.com/36766101/212474081-b6a52f3f-4b61-4d96-86f9-3414465c34a7.png)

Events
An event is a real-time change in a system, data, or environment. This change can be either in your application or in an AWS service or a SaaS partner service.

Event sources
An event source is used to ingest events from a SaaS partner, AWS Services, or your own applications.

Event buses
An event bus is a pipeline that receives events. Rules associated with the event bus evaluate events as they arrive. Each rule checks whether an event matches the rule’s criteria.

Rules
A rule matches incoming events and sends them to targets for processing. A single rule can send an event to multiple targets, which then run in parallel.


Targets
A target is a resource or endpoint that EventBridge sends an event to when the event matches the event pattern defined for a rule. The rule processes the event data and sends the pertinent information to the target. To deliver event data to a target, EventBridge needs permission to access the target resource. You can define up to five targets for each rule.


![image](https://user-images.githubusercontent.com/36766101/212467520-5e117073-21d0-42b0-a326-49e9e0c455ab.png)
![image](https://user-images.githubusercontent.com/36766101/212468993-85cb9aa9-330d-46a3-975d-1568620e0c30.png)
![image](https://user-images.githubusercontent.com/36766101/212473006-4b9865c2-24dd-40e6-8ed6-79acc0e7bd15.png)



# Dynamodb Table scan
aws dynamodb scan --table-name ga4_offline_event --filter-expression 'begins_with(event_time,:event_time) AND event_name = :event_name' --expression-attribute-values '{ ":event_name" : {"S": "payingOrg"}, ":event_time" : {"S": "2023-01-13"} }'  --select "COUNT" --region=ap-southeast-2


aws dynamodb query --table-name ga4_offline_event  --key-condition-expression "begins_with(event_time,:event_time) AND event_name = :event_name" --expression-attribute-values '{ ":event_name" : {"S": "user_created"}, ":event_time" : {"S": "2023-01-09"} }'  --select "COUNT" --region=ap-southeast-2

![image](https://user-images.githubusercontent.com/36766101/213093362-0b36f721-2e45-4ee8-84d8-e0d6eff985f1.png)



# AWS cloudwatch log insight to query log result and export 

fields @message 
    | filter @message like /payingOrg/ 
    | stats count(*) as total_count by bin(1h)
    | sort total_count desc
    | limit 10000
![image](https://user-images.githubusercontent.com/36766101/213669747-5fbdf96a-b39b-4db7-9123-8e3efc10550a.png)


# AWS Dyanmodb Point-in-time recovery (PITR) and use AWS backup to create backup protection (2023/01/21)
![image](https://user-images.githubusercontent.com/36766101/213830802-29a72ae4-ddd4-4303-8899-1466fd527748.png)
![image](https://user-images.githubusercontent.com/36766101/213830806-6579ce0d-8166-4627-bdc6-a1750272ce58.png)





# AWS DR solution （2023/01/27）
Determine your RPO/RTO requirements to choose which option you 
Pilot Light
![image](https://user-images.githubusercontent.com/36766101/214968280-155a056d-a3a2-4b5b-b063-01180d4b8aaf.png)
![image](https://user-images.githubusercontent.com/36766101/214970029-35b4cae5-ab1e-4dc1-b7d7-fc7044a43f74.png)
![image](https://user-images.githubusercontent.com/36766101/214979171-314c2fc2-db67-4616-9979-82303c7af18b.png)
![image](https://user-images.githubusercontent.com/36766101/214984796-98c6790a-ce11-4603-864c-6ecb2e4b5a18.png)
![image](https://user-images.githubusercontent.com/36766101/214991618-c7a06da8-5940-40f7-95a7-88c0aded4d69.png)
Route53 health check for failover DNS and Use SG of LB to simulate site failure.
![image](https://user-images.githubusercontent.com/36766101/214994148-524e288d-1eae-4a9b-9492-9a6733a66c13.png)
![image](https://user-images.githubusercontent.com/36766101/214996736-10936c63-7eea-453a-8e56-89feb9186f1a.png)
![image](https://user-images.githubusercontent.com/36766101/214998620-d3e02bea-ecab-4a19-8300-7a791bead2c5.png)
Multi-region Active/Active
![image](https://user-images.githubusercontent.com/36766101/214999172-02ab72c2-e41b-4c8f-b80e-d16b271a7615.png)
![image](https://user-images.githubusercontent.com/36766101/214999361-53020233-dfbe-4b6c-aa7f-1f2cdc809d12.png)
Route53 latency routing policy
![image](https://user-images.githubusercontent.com/36766101/215000313-aa46e945-25b7-4544-8130-79b9c8a40c37.png)
![image](https://user-images.githubusercontent.com/36766101/215000473-6eea9c50-e4ff-4cbf-ba7d-5bcc7ffd0742.png)

Aurora Global Database
![image](https://user-images.githubusercontent.com/36766101/215016111-0bf2d564-d5af-425d-b25c-ce2d6d49c26c.png)
![image](https://user-images.githubusercontent.com/36766101/215016034-8e4c17a1-0998-44c5-a681-ad5b1bc94562.png)
![image](https://user-images.githubusercontent.com/36766101/215016946-99f6c3e7-ca58-43c6-94cd-bf01ba26d88b.png)
Relational Database Failback Options
Scenario
Primary Database is in one region, and for disaster recovery, there is a cross-region read replica in the second region

![image](https://user-images.githubusercontent.com/36766101/220032270-b672794b-70d3-422a-bb68-f5cd12a73111.png)
Disaster Recovery When Primary is Down
When the primary region is down, you would detach the read replica in the DR region and promote it as a new primary

At this point, this new primary is a separate system (in the DR region), and you would need to set up a new cross-region read replica

The old primary database is no longer used

Failback to Primary Region
To failback to the primary region, you would need to have a cross-region read replica in the primary region

And failback process depends on the relational product used

With Aurora Global Database, when you do a managed failover to a different region, primary and cross region read-replica roles are reversed. This option is the easiest and cleanest

If you use any other relational database, you would have to disconnect the read-replica in the primary region and promote it as the primary database. You then need to configure a read-replica for this new primary.

ClickStream analyse using Kinesis data stream and Lambda

![image](https://user-images.githubusercontent.com/36766101/215632086-9d9d3f9e-c03e-40ad-966d-ec7c0f59bbe0.png)

![image](https://user-images.githubusercontent.com/36766101/215631957-208d4bb5-769a-47c9-b659-5f41801baf45.png)


To determine your IP use dig
dig +short myip.opendns.com @resolver1.opendns.com
![image](https://user-images.githubusercontent.com/36766101/218381733-8d41db3d-21e0-4388-9c4c-7ce88841f48d.png)


# AWS Security Hub  and other security products such as AWS Inspector(Inspector agent installed on EC2) and and AWS Config and GuardDuty (2023/02/20) 
Security hub can ingest findings from different AWs products include AWS Config/AWS Firewall Manager/AWS GuardDuty/AWS Macie/AWS Inspector/AWS Health/AWS IAM Analyzer/AWS SSM Patch Manager and can egress data to AWS Audit Manager/Amazon Detective/AWS SSM OpsCenter and Explorer/AWS EventBridge/AWS Trust Advisor.

AWS Security Hub sends its findings to Trusted Advisor.

Detective is a service that helps you analyze and investigate the root cause of security findings or suspicious activity. Using data from AWS Cloudtrail logs, VPC flow logs and AWS GuardDuty data, Amazon Detective will collate, filter the collected security data and using AWS Security Hub, GuardDuty, integrated partner security products, machine learning and statistical analysis investigates the security findings to get to the root cause of the problem or suspicious activity.

![image](https://user-images.githubusercontent.com/36766101/221713364-78359c9f-f8c3-4971-9d92-5a2cf29935e2.png)


![image](https://user-images.githubusercontent.com/36766101/221393297-a212bfb8-711b-4bab-92e9-1dd4e1f1ead2.png)
![image](https://user-images.githubusercontent.com/36766101/221393392-d263d3b5-1d13-415f-a462-5aa40b68f189.png)
![image](https://user-images.githubusercontent.com/36766101/221393843-08fb1a80-d6e7-4220-8eba-0b6af59bb900.png)

![image](https://user-images.githubusercontent.com/36766101/221387075-76b28861-8c77-447c-b560-40ee6af88d56.png)

![image](https://user-images.githubusercontent.com/36766101/220090134-a579cc45-edaa-4daa-b804-fd24878d7363.png)
![image](https://user-images.githubusercontent.com/36766101/220767065-d09a01a9-5b1a-46b3-8606-1aed1221c931.png)

![image](https://user-images.githubusercontent.com/36766101/219993213-5c9b1e79-bfe5-4abf-b1c5-71c736eb7be2.png)
![image](https://user-images.githubusercontent.com/36766101/219995808-9de7769a-bd14-4f41-aff2-a726f3c5afcc.png)
![image](https://user-images.githubusercontent.com/36766101/220001017-4a5fde7f-29a3-4c8b-8d2e-ace8c1a6a004.png)
![image](https://user-images.githubusercontent.com/36766101/220030600-9a3ab4f8-4b3f-4d3d-874b-0ec9c20c59e3.png)
![image](https://user-images.githubusercontent.com/36766101/220031454-f5664a80-cf34-4f04-a180-8efca3cdbf5a.png)
![image](https://user-images.githubusercontent.com/36766101/220034157-850e65a5-4917-4a0d-85a4-03efed00ea37.png)
![image](https://user-images.githubusercontent.com/36766101/220034274-d8874c46-efb1-49e5-a996-9d2610a1a08c.png)
![image](https://user-images.githubusercontent.com/36766101/220038276-31fff420-9077-4e35-9584-074b69ec72bc.png)
![image](https://user-images.githubusercontent.com/36766101/220082861-7012014a-3827-4138-a030-e28362fed802.png)
![image](https://user-images.githubusercontent.com/36766101/220085183-3d5c0aa1-0881-40a2-88ba-246665276f55.png)
![image](https://user-images.githubusercontent.com/36766101/220088171-fcfe4f9d-c129-469b-b26f-4ad11d7874fa.png)
![image](https://user-images.githubusercontent.com/36766101/220093699-4f6a37c2-3cef-4262-b6d8-19a9617984dc.png)
![image](https://user-images.githubusercontent.com/36766101/220203287-3110e5f3-1321-42d4-b17a-0983e013dee1.png)
![image](https://user-images.githubusercontent.com/36766101/220205340-04713f9b-ff70-4b02-a0c1-ad8247e703e0.png)
![image](https://user-images.githubusercontent.com/36766101/220205796-1cf0207e-8873-4e88-8829-f149563570e6.png)

![image](https://user-images.githubusercontent.com/36766101/221408610-e6474ad3-40e3-4332-a877-b932684f9c65.png)
![image](https://user-images.githubusercontent.com/36766101/221408688-b2cbc2c0-03a4-4079-87b8-fcadd860fe12.png)
![image](https://user-images.githubusercontent.com/36766101/221409966-24146904-c5da-4f67-8039-9f9e473444ca.png)
![image](https://user-images.githubusercontent.com/36766101/221409996-63b89b22-823b-4949-8f68-260d4f4b725d.png)

https://aws.amazon.com/blogs/security/how-to-visualize-multi-account-amazon-inspector-findings-with-amazon-elasticsearch-service/
https://controltower.aws-management.tools/security/guardutydetect-securityhubremediate/

# Executing Automation Workflow Using AWS SSM Automation    (2023/02/20) 
https://github.com/xiongye77/aws_sysops_tasks/blob/main/ssm-automation.json
![image](https://user-images.githubusercontent.com/36766101/220005717-496826d9-5c71-4a0a-b108-692c6d07b04e.png)
![image](https://user-images.githubusercontent.com/36766101/220007995-ff7ea152-27b6-43a3-aabc-31f57afe36a8.png)
![image](https://user-images.githubusercontent.com/36766101/220008073-fd22884f-8b79-45ab-bc07-6ff178d9d822.png)


# Security your S3 from A to Z
![image](https://user-images.githubusercontent.com/36766101/220063999-6e63b017-d6d0-4944-ab89-144631c6b51d.png)
use cloudtrail data event only log data event to specific bucket
![image](https://user-images.githubusercontent.com/36766101/220074340-cdb79f0a-f525-419c-9a92-67822f65764c.png)
![image](https://user-images.githubusercontent.com/36766101/220209105-14235f1c-0cea-459a-8756-03e0688089eb.png)
![image](https://user-images.githubusercontent.com/36766101/220209823-98260b38-5db4-46f1-94cb-7982dc075de4.png)
![image](https://user-images.githubusercontent.com/36766101/220210358-24830dea-672e-4d7e-bc89-8308e22d74fb.png)



# AWS Landing Zone and Control Tower and Guardrail
![image](https://user-images.githubusercontent.com/36766101/220476946-6d1b6e9f-d542-4db1-8c70-cd7a23fd08c7.png)
![image](https://user-images.githubusercontent.com/36766101/220477110-39c06959-2b72-4cc0-b798-1b62d1430f77.png)
![image](https://user-images.githubusercontent.com/36766101/220527605-719bb5b8-7c69-439e-8b57-37f0904a6078.png)
![image](https://user-images.githubusercontent.com/36766101/221493878-f3fec282-a6fd-48f6-9dda-44410ab7170b.png)
![image](https://user-images.githubusercontent.com/36766101/221494146-f96c89b1-b401-49b2-9d01-109d5840646a.png)
![image](https://user-images.githubusercontent.com/36766101/221496375-5cd9e18e-4b7c-45fb-a88c-e1ec600f7c44.png)
![image](https://user-images.githubusercontent.com/36766101/221496934-b6d8c21f-3379-4426-aa8f-bc70333542c5.png)
![image](https://user-images.githubusercontent.com/36766101/221497484-a7cf341a-3942-4a61-bcd9-8ff342d74e44.png)



# Deny execution of non-compliant images on EKS/ECS using AWS Security Hub and ECR (2023/02/23)
https://github.com/xiongye77/aws_sysops_tasks/blob/main/ecr-compliance.yaml
![image](https://user-images.githubusercontent.com/36766101/220838784-485bd949-8be3-449a-90e7-8f3d46b08b18.png)

![image](https://user-images.githubusercontent.com/36766101/220838435-1e622cdd-4995-4d0d-9a1c-39c6e11acbce.png)
![image](https://user-images.githubusercontent.com/36766101/220838620-d3ed0dff-8843-43df-b16d-65eff482b876.png)
![image](https://user-images.githubusercontent.com/36766101/220838689-53d354f3-f290-44b3-a741-8875b02da72c.png)

![image](https://user-images.githubusercontent.com/36766101/220837961-2e2c3577-5d8a-4158-a641-bff3dad10d88.png)
![image](https://user-images.githubusercontent.com/36766101/220838281-1fa7218c-9f7d-4278-ad6c-b30ac9a606a6.png)


![image](https://user-images.githubusercontent.com/36766101/220838359-d0dba3e1-3941-4733-b247-9fd1ba3be13f.png)

![image](https://user-images.githubusercontent.com/36766101/220839188-3a2ee99d-7c4c-4f1c-9ef6-f02977c0086d.png)


# AWS SSM OpsCenter 
![image](https://user-images.githubusercontent.com/36766101/220872211-7ef50820-9744-47e6-b4cd-63d1a57876b7.png)



# AWS Security Hub check for Center for Internet Security/Payment Card Industry Data Security Standard/

![image](https://user-images.githubusercontent.com/36766101/221387578-00965def-cc5a-418e-87ec-1b7f1edec6bf.png)


# AWS Organization/OU/SCP
![image](https://user-images.githubusercontent.com/36766101/224846476-15a5d224-6568-4cd7-a443-d6fc038b8bf9.png)

![image](https://user-images.githubusercontent.com/36766101/221395413-002565d3-a590-40eb-962e-740628c7baa6.png)
![image](https://user-images.githubusercontent.com/36766101/221395426-1e5a11f3-2064-4b50-8089-b00ea20894d1.png)
![image](https://user-images.githubusercontent.com/36766101/221395665-55a68565-0445-4947-873c-fb91a74ddbbf.png)

# Query Cloudtrail log on S3 use Athena (partition projection for CloudTrail logs with Athena) Or to Cloudwatch and to ElasticSearch
![image](https://user-images.githubusercontent.com/36766101/221395820-76943082-3a90-40a4-b5ac-c28b7446e2a9.png)
https://aws.amazon.com/premiumsupport/knowledge-center/athena-tables-search-cloudtrail-logs/


# Service control policy attach to OU or Organization to control only launch specific type of EC2 instance
![image](https://user-images.githubusercontent.com/36766101/221493741-4b1f02bc-da7a-4d82-ba26-4a39e21009c5.png)

![image](https://user-images.githubusercontent.com/36766101/221479909-548f1915-f684-494c-a9ec-a60c55c476d2.png)
![image](https://user-images.githubusercontent.com/36766101/221480664-9584df6e-e9b9-47ec-85b6-3ba7361b9263.png)


# AWS Identity Federation 
![image](https://user-images.githubusercontent.com/36766101/221486581-37e46c03-676f-4d6d-ac6d-5a3a229bb986.png)
![image](https://user-images.githubusercontent.com/36766101/221490746-8ba3388d-9b70-4d0e-b602-455a26c96b24.png)
![image](https://user-images.githubusercontent.com/36766101/221490819-78304b7a-c659-47b3-9672-c9f32dc99de9.png)


![image](https://user-images.githubusercontent.com/36766101/221485431-7e586ed3-4f74-4e68-8a27-e401add0e63e.png)


# AWS SSM Document and Inventory for log4j (2023/03/02)

![image](https://user-images.githubusercontent.com/36766101/222339635-7539a175-26f1-4bf9-b55c-dd310881cb95.png)
![image](https://user-images.githubusercontent.com/36766101/222340014-e8ea8fe6-9397-4b82-8da9-98adb6ac4463.png)
![image](https://user-images.githubusercontent.com/36766101/222342160-4a32c894-6e19-4881-b454-d176d14d8b23.png)
![image](https://user-images.githubusercontent.com/36766101/222346163-9bdde78e-2ac7-4d19-a648-e23f377b7c87.png)

# AWS SG/NACL/WAF/Firewall Manager  (2023/03/03)
![image](https://user-images.githubusercontent.com/36766101/222422994-cb623917-7c5e-499b-ad92-d13293a81e58.png)
![image](https://user-images.githubusercontent.com/36766101/222427971-685e311b-18e2-4b2c-a0cf-f94829f1ccaa.png)
![image](https://user-images.githubusercontent.com/36766101/222428291-6c77e656-2527-421e-8e7a-9cff8d5e3253.png)
![image](https://user-images.githubusercontent.com/36766101/222557503-f89e6d0f-c572-4434-b6c3-e97a6281e9b1.png)
![image](https://user-images.githubusercontent.com/36766101/222558410-40609756-80c9-4bef-9200-611f8da510d8.png)


# EC2 Reset passwords and SSH keys on EC2 instances (2023/03/10)
https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2reset.html#automation-ec2reset-how
![image](https://user-images.githubusercontent.com/36766101/224241045-de31ed2c-fa9d-4c7e-bf35-63358ba4e2d9.png)


# AWS VPC private link (VPC endpoint service) (2023/03/10)
![image](https://user-images.githubusercontent.com/36766101/224284676-742f2ed9-3ced-45de-af30-f20f891f3f52.png)
![image](https://user-images.githubusercontent.com/36766101/224284833-2d501ee2-19ea-4c74-b0f7-290594360d1c.png)


# AWS Cloudfront Signed URL (2023/03/10)
![image](https://user-images.githubusercontent.com/36766101/224848739-73fd58e6-9070-40d6-aaaf-8dbea351e7bc.png)

![image](https://user-images.githubusercontent.com/36766101/224286591-af58d25d-09ae-4790-a5f0-7412da619d27.png)
![image](https://user-images.githubusercontent.com/36766101/224287561-01b4b9f8-4e8c-4207-b387-8c01021fa078.png)


# AWS Firewall Manager and Network Firewall  (2023/03/10)
![image](https://user-images.githubusercontent.com/36766101/224289049-a27e5f74-29f6-49d3-9fc6-c5e64a0bfbb9.png)
![image](https://user-images.githubusercontent.com/36766101/224289117-7f23c518-8753-4456-964f-8e4e790ab716.png)
![image](https://user-images.githubusercontent.com/36766101/224292137-fcfa26ca-e8de-4b6d-8298-ee2a4bac1300.png)
![image](https://user-images.githubusercontent.com/36766101/224304445-fa445282-db8e-49da-ad99-07702ae6c616.png)
![image](https://user-images.githubusercontent.com/36766101/224304926-e8d1a211-0c43-409a-8a33-e67b3d181a35.png)


# AWS EC2 Instance Metadata
![image](https://user-images.githubusercontent.com/36766101/224306150-01564bf4-97ed-4043-b18b-e645437449b4.png)
![image](https://user-images.githubusercontent.com/36766101/224306649-3b2d5d73-1798-452e-9ab0-8888ce29b046.png)

# AWS S3 CROS
![image](https://user-images.githubusercontent.com/36766101/224309589-08c782e0-c188-4f5a-a069-3265e518faa2.png)
![image](https://user-images.githubusercontent.com/36766101/224311979-c602aa95-6560-4b3b-a228-40f6cb853c50.png)


# AWS Glue
![image](https://user-images.githubusercontent.com/36766101/224619038-d702d924-2acc-4292-9d7a-febe130dfb81.png)
![image](https://user-images.githubusercontent.com/36766101/224619405-3c88eef6-2c58-48e1-a0d3-d514598ae13f.png)
![image](https://user-images.githubusercontent.com/36766101/224622106-166c8f5d-055c-4a49-bb66-76dd10c99dcc.png)
![image](https://user-images.githubusercontent.com/36766101/224623037-9479daf9-535b-4046-bbf5-813e19e55da7.png)

# AWS Asymmetric Encryption
![image](https://user-images.githubusercontent.com/36766101/224907933-fdd2efcd-c8ad-418e-a2c7-4a0fd428f524.png)


# AWS Resource Group
![image](https://user-images.githubusercontent.com/36766101/225219697-d07241ff-921c-4818-b86d-a0ae5fccc579.png)

# AWS Creating an AWS Budget and Billing Alarm
![image](https://user-images.githubusercontent.com/36766101/225229316-54010855-6ef9-4129-a3db-0e2797b0ddde.png)


# AWS compute optimizer
![image](https://user-images.githubusercontent.com/36766101/225272121-43780238-1bd5-418b-9c29-bd646c576850.png)

# AWS EC2 placement group
![image](https://user-images.githubusercontent.com/36766101/225278718-87c11133-9f65-41f8-8df0-a50d102e741e.png)

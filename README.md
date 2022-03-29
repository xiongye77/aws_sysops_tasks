# AWS cost optimization 


Deploy and enable Cost Anomaly Alerts to your AWS organization payer account.Make sure you have slack channel prepared as parameter for 
defaultSlackWebhookURL	https://hooks.slack.com/services/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   
https://github.com/ighanim/aws-cost-anomaly-alerts

![image](https://user-images.githubusercontent.com/36766101/159828197-6f239317-6af7-46c5-ad9f-ffd2cdf7f8ca.png)
![image](https://user-images.githubusercontent.com/36766101/159828368-566f4a80-45f1-4fd8-834b-b3a0bf0b0745.png)
![image](https://user-images.githubusercontent.com/36766101/159828396-eea4787d-31e2-425b-bd1f-417db0ac1154.png)



Disable EC2 instance detailed monitor since we have new relic for performance and Sumologic for log analyze.
https://github.com/xiongye77/aws_sysops_tasks/blob/main/disable_ec2_detailed_monitor.py


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


AWS S3 presigned url for temporary access of private contents.

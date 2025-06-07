# AWS SYS OPS  

# AWS Config and Cloudtrail records all assets with related tag(s) have any changes (2025/06/07)
0. Enable AWS config and Cloudtrail , add tag for your assets, in this example , add key value pair as System ProdCore
1. Create Event Bridge Rule to record aws config changes
   <img width="1536" alt="image" src="https://github.com/user-attachments/assets/8b5ea749-8337-4ba4-8800-8d9e3ba03855" />

2. Set destination for the event, using lambda function
   <img width="1512" alt="image" src="https://github.com/user-attachments/assets/5645efd4-21cc-4610-a0cc-b4c8f63e9499" />

3. Create lambda function to parse the aws config event comes in, also search in cloudtrail ,send all results to SNS topic and store in DynamoDB
https://github.com/xiongye77/aws_sysops_tasks/blob/main/post-aws-config-change-sns.py
<img width="1458" alt="image" src="https://github.com/user-attachments/assets/e3e3600a-ac6a-44fe-b823-0746f177f2bc" />
<img width="1681" alt="image" src="https://github.com/user-attachments/assets/7f0b604c-42b1-42b0-b1fc-164fe7fc943b" />
<img width="1278" alt="image" src="https://github.com/user-attachments/assets/3d279eda-f400-4463-8922-83c660f87c5d" />
<img width="1441" alt="image" src="https://github.com/user-attachments/assets/f8510e78-6a70-493f-a74b-12f4f530603d" />
<img width="1660" alt="image" src="https://github.com/user-attachments/assets/b387eb62-934f-485c-8226-683d9a3341d3" />

# How Azure function/VM access AWS S3 without using long-term credentials (2025/06/06)

![image](https://github.com/user-attachments/assets/336f56e2-e087-4d4b-8f29-97600f59b958)
![image](https://github.com/user-attachments/assets/fe443d98-cdf5-4b52-b372-cb190256b92d)

<img width="810" alt="image" src="https://github.com/user-attachments/assets/bc887f49-8c18-4bdc-a208-e6d5b185eeb3" />
<img width="1181" alt="image" src="https://github.com/user-attachments/assets/72c51faf-c928-49b1-87f4-248d448d2bd0" />

# How to use web identity federation authenticated by Google and with Cognito identity pool to access AWS S3 (2025/06/05)
<img width="1133" alt="image" src="https://github.com/user-attachments/assets/7b6a41e0-bc07-4727-94ef-d00ffdc9a528" />


# MSK Connect connector
Amazon MSK Connect is a fully managed service that allows you to stream data between Apache Kafka and other data sources or sinks. It simplifies the process of integrating data streams with various AWS services and external systems by providing a scalable, reliable, and easy-to-use platform.


<img width="1577" alt="image" src="https://github.com/user-attachments/assets/20c47015-4978-4f43-84e0-0f27cd570d6f" />
<img width="1400" alt="image" src="https://github.com/user-attachments/assets/c80b0b8b-d463-439f-a634-c7438ac1b41b" />


1. Source Connectors
We will use Kafka Connect along with three Debezium connectors, MySQL, PostgreSQL, and SQL Server, to connect to three corresponding Amazon Relational Database Service (RDS) databases and perform CDC. Changes from the three databases will be represented as messages in separate Kafka topics. In Kafka Connect terminology, these are referred to as Source Connectors. According to Confluent.io, a leader in the Kafka community, “source connectors ingest entire databases and stream table updates to Kafka topics.”

Enabling CDC for Amazon RDS
To use Debezium for CDC with Amazon RDS databases, minor changes to the default database configuration for each database engine are required.

CDC for PostgreSQL
Debezium has detailed instructions regarding configuring CDC for Amazon RDS for PostgreSQL. Database parameters specify how the database is configured. According to the Debezium documentation, for PostgreSQL, set the instance parameter rds.logical_replication to 1 and verify that the wal_level parameter is set to logical. It is automatically changed when the rds.logical_replication parameter is set to 1. This parameter is adjusted using an Amazon RDS custom parameter group.

2. Sink Connector
We will stream the data from the Kafka topics into Amazon S3 using a sink connector. Again, according to Confluent.io, “sink connectors deliver data from Kafka topics to secondary indexes, such as Elasticsearch, or batch systems such as Hadoop for offline analysis.” We will use Confluent’s Amazon S3 Sink Connector for Confluent Platform. We can use Confluent’s sink connector without depending on the entire Confluent platform.






# Ausora Postgres Replication monitor replication lag 
![image](https://github.com/user-attachments/assets/61a4f0ec-dbde-4a2a-8a9a-e1fa6f2af272)
<img width="1347" alt="image" src="https://github.com/user-attachments/assets/1579dc0a-011c-4e37-87a4-db0b3ffea720" />
<img width="949" alt="image" src="https://github.com/user-attachments/assets/c0f73880-ddd5-4fc2-8344-9eeb69cb6814" />

# Aurora Postgres Audit (2025/05/21)
<img width="1202" alt="image" src="https://github.com/user-attachments/assets/23b28237-71c9-4c11-b8e5-65c823641654" />

<img width="925" alt="image" src="https://github.com/user-attachments/assets/7db71336-cc42-4e7f-95b1-4a583d5a88a3" />

![image](https://github.com/user-attachments/assets/1b27f4cf-7c65-42d2-a0a1-8b6a9fa613ed)
<img width="1372" alt="image" src="https://github.com/user-attachments/assets/cbbe69e2-cc57-41ec-af79-a89e5200d2c7" />
<img width="1407" alt="image" src="https://github.com/user-attachments/assets/f4d8a0aa-dabe-4e32-937c-853136d20a7a" />

# MSK(producer/consumer) Glue schema registry (2025/05/20)
https://github.com/xiongye77/aws_sysops_tasks/blob/main/glue_schema_registry_producer_consumer.py
![image](https://github.com/user-attachments/assets/c22e8493-2ec1-4720-b4ee-c29e595c1ed8)
<img width="990" alt="image" src="https://github.com/user-attachments/assets/7a840dfd-6043-4832-b863-9eefe77faff0" />
<img width="1622" alt="image" src="https://github.com/user-attachments/assets/09382330-f6e1-40d3-8196-cb7838db471d" />

# Kafka TOPIC/PARTITION/HOST （2025/05/18）
https://github.com/xiongye77/aws_sysops_tasks/edit/main/kafka_consumer_topic.py
host : The IP address or hostname of the client machine (consumer) that is actively consuming data from that partition.
<img width="1728" alt="image" src="https://github.com/user-attachments/assets/3debdb7e-a189-48e9-9ac4-1248b4d26e36" />
Lag = log-end-offset − current-offset
It represents the number of messages a consumer has not yet processed in a given partition.Monitoring Kafka consumer lag is absolutely essential for maintaining a healthy stream data pipeline


Kafka brokers always retain messages according to the topic’s retention settings, regardless of whether any consumer has read them. Consumers simply track their own offsets; they do not tell the broker to delete messages when they consume them.

When messages actually get removed

1. log.retention.ms passes → broker deletes the segments.

2. log.retention.bytes exceeded → broker deletes oldest segments to free space.


# MSK broker scale out and scale up 
<img width="822" alt="image" src="https://github.com/user-attachments/assets/af93349c-7a9c-45ae-8f70-2f7c905fb856" />
# MSK cross account access 
<img width="1093" alt="image" src="https://github.com/user-attachments/assets/6d7c0cee-228e-46c0-8966-c764086e94c6" />
1. MSK cluster owner to enable PrivateLink connectivity on the MSK cluster and select authentication schemes to control access to the cluster.
2. The cross-account user will connect privately to the MSK cluster using IAM auth scheme.
3.The cluster owner turns on multi-VPC private connectivity on the ACTIVE cluster for any auth schemes that will be active on the cluster. 
4. Attach a cluster policy to the MSK cluster
5. In the MSK console for the client Account B, choose Managed VPC connections, and then choose Create connection.
# MSK tiered storage node
<img width="752" alt="image" src="https://github.com/user-attachments/assets/4992b650-60b0-4fae-98c1-1d8914033d3a" />
# MSK connector 
Streaming RDS changes into Kafka—often via a CDC (Change Data Capture) pipeline—is extremely common because it unlocks many architectural and operational benefits:

1. Decoupling of Systems & Asynchronous Processing
By capturing inserts/updates/deletes from your RDS and publishing them as Kafka events, you decouple your transactional database from downstream consumers. Instead of having every service hit the RDS for real‑time data, they subscribe to the Kafka topic and process events at their own pace. This reduces load on your database and avoids tight coupling.


2. Real‑Time Data Propagation
Traditional ETL jobs run on schedules (hourly, nightly). CDC into Kafka delivers changes within seconds of commit in RDS, so analytics dashboards, caches, search indexes, or other microservices always see the freshest data.

3. Scalability & Fan‑Out
Kafka topics can have many independent consumers—analytics pipelines, audit logs, search indexing, materialized views, notification systems, etc.—all consuming the same change stream without impacting the RDS. You simply add new consumers rather than overloading your database


4. Event‑Driven Architectures
Publishing RDS changes to Kafka lets you treat each data change as an event. Services can react (e.g., update a user’s recommendation, recalculate aggregates, trigger alerts) in a natural, event‑driven way, improving responsiveness and modularity.

5. Auditability & Replay
Kafka retains your change events for a configurable window. If you need to rebuild a cache or replay historical changes for a new service, you simply rewind the consumer offset. You wouldn’t get that easily from querying RDS

Typical CDC flow for RDS → Kafka
Enable logical or binlog replication on the RDS instance.

Run a CDC connector (e.g., Debezium) that tails those logs and publishes events into Kafka topics.

Consumers subscribe to those topics (real‑time consumers like Kafka Streams, KSQL, or applications) to process the changes.

# MSK broker metric
<img width="811" alt="image" src="https://github.com/user-attachments/assets/811dfd07-ca68-4a4e-9797-98710b63104c" />

# Scale MSK brokers and rebalancing paritions across new broker nodes
<img width="1267" alt="image" src="https://github.com/user-attachments/assets/be8efd61-740c-46f4-b2b8-84808b045727" />
1. Get the current assignment  bin/kafka-topics.sh --bootstrap-server <broker-list>  --describe --topic your-topic > current_assignment.txt
2. Use a helper script to generate the JSON bin/kafka-reassign-partitions.sh  --bootstrap-server <broker-list>  --generate --topics-to-move-json-file topics-to-move.json --broker-list "1,2,3,4"
3. Execute the reassignment bin/kafka-reassign-partitions.sh  --bootstrap-server <broker-list>  --execute  --reassignment-json-file reassign.json
4. Validate progress  bin/kafka-reassign-partitions.sh --bootstrap-server <broker-list>  --verify  --reassignment-json-file reassign.json


# AWS Inspector scan for EC2/ECR/Lambda 
![image](https://github.com/user-attachments/assets/3c4e9c26-9d8d-4111-9e81-e01f6f140ecd)
<img width="1336" alt="image" src="https://github.com/user-attachments/assets/fbf49525-7565-4f20-ac23-9fadf1d8ea97" />
<img width="1377" alt="image" src="https://github.com/user-attachments/assets/19b05862-dbee-4e90-903d-389c3c414df7" />
<img width="826" alt="image" src="https://github.com/user-attachments/assets/5b81813e-0b22-4fb6-98bf-7e1021ea64cb" />
Instead of one by one run the upgrade command We can run upgrade command using SSM  AWS-RunShellScript Run command to upgrade a bunch of EC2 instances

<img width="611" alt="image" src="https://github.com/user-attachments/assets/9335b748-d843-401b-9715-93ca5a8ab434" />
<img width="828" alt="image" src="https://github.com/user-attachments/assets/ee7f0cbe-69f2-4a84-94c0-b7cadd5a485d" />

After upgrade and uninstall old packages, perform a manually refresh software inventory 
<img width="787" alt="image" src="https://github.com/user-attachments/assets/7b760d0d-3c0b-4e51-a6e5-2d77d8c84686" />

# AWS SSM maintenance Window to run AWS-RunPatchBaseline to install patches for EC2 

<img width="1424" alt="image" src="https://github.com/user-attachments/assets/0c8f2329-0d3b-47de-ae6b-a4c8957c3b30" />



# AWS SSM patch manager to create patch policy (formal name: Patch Baseline + Patch Group + Maintenance Window)
<img width="1461" alt="image" src="https://github.com/user-attachments/assets/90ee3999-0025-4388-bc4f-46bebd96d229" />
<img width="1236" alt="image" src="https://github.com/user-attachments/assets/69c6f137-f209-4ac4-b820-c635f249ac66" />
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/cd46ad2e-9bbe-4adf-a62e-313d6cf847fb" />

# AWS Config Conformance Packs
<img width="1202" alt="image" src="https://github.com/user-attachments/assets/da275114-24d7-4737-b025-c1e96f63827a" />
<img width="1142" alt="image" src="https://github.com/user-attachments/assets/b3611720-8a02-4443-ba5a-8956cdb69c8a" />
https://github.com/xiongye77/aws_sysops_tasks/blob/main/RDSCompliancePack.yaml


# Amazon GuardDuty S3 Malware Protection
When we enable the Amazon GuardDuty S3 Malware Protection, there is an Amazon EventBridge rule is created that watches put object events. When we upload an object, this rule catches the event and sends details to the malware scan service on the AWS side.
<img width="1657" alt="image" src="https://github.com/user-attachments/assets/bff7edb7-a081-48e9-8c81-af434638bedd" />
<img width="1006" alt="image" src="https://github.com/user-attachments/assets/cc7a401e-937a-4b63-b227-3d03edc44ff7" />
<img width="1005" alt="image" src="https://github.com/user-attachments/assets/a0a1edf1-3dd6-469b-a40c-642b1bd18e67" />



# AWS Security Lake gather logs with Cloudtrail/VPC Flow log/Security Hub/EKS/WAF
<img width="1698" alt="image" src="https://github.com/user-attachments/assets/dc06b38e-f252-4c19-be04-c1ac7810418e" />

<img width="1691" alt="image" src="https://github.com/user-attachments/assets/2cfa54f1-91c1-42af-b0bf-d781a739bd78" />
Amazon Security Lake automatically converts the data format of native AWS services to OCSF.OCSF (Open Cybersecurity Standards Framework) schema provides a structured and standardized way to represent cybersecurity data. This universal language allows various cybersecurity tools to interact seamlessly, making it easier for organizations to integrate solutions from different vendors.

# Centralized inspection with AWS GWLB – Inter VPC traffic
east-west traffic within AWS network 
<img width="1298" alt="image" src="https://github.com/user-attachments/assets/07f10629-734c-4e31-909c-0c9f47ad7a08" />


# Centralized inspection with AWS GWLB – internet traffic
north-south traffic into internet 
<img width="1291" alt="image" src="https://github.com/user-attachments/assets/2b3a367f-30ff-421b-bc80-51752b4ec858" />

# Route53 DNSSEC 
<img width="1310" alt="image" src="https://github.com/user-attachments/assets/a913f42a-ee8a-407b-9730-69bead63d24b" />


# Route53 DNS resolver
<img width="1291" alt="image" src="https://github.com/user-attachments/assets/abef5d7b-a86a-4823-ba79-087164bbb934" />
<img width="1288" alt="image" src="https://github.com/user-attachments/assets/81740c9e-0224-483a-be53-fa37c2c53d5b" />
<img width="1287" alt="image" src="https://github.com/user-attachments/assets/1f5d07a0-401d-48ae-a074-0049c116d9d8" />
<img width="1274" alt="image" src="https://github.com/user-attachments/assets/c02d5a41-4df2-41c5-861b-431f9d77f67d" />
<img width="1255" alt="image" src="https://github.com/user-attachments/assets/1d687158-92e9-4b19-9f4d-82e8d2369250" />
<img width="1685" alt="image" src="https://github.com/user-attachments/assets/1b4b74c7-6c4c-4e90-be69-eef036a36b09" />


# Route53 resolver firewall
<img width="832" alt="image" src="https://github.com/user-attachments/assets/c9433ef3-1681-4d9d-a807-dc828ab642ea" />
<img width="876" alt="image" src="https://github.com/user-attachments/assets/a023de4b-baf9-4f95-a037-fa1349b6733f" />
<img width="1071" alt="image" src="https://github.com/user-attachments/assets/f3a2bd27-aa4e-4821-a42f-c5d0fd87722f" />

# Transit gw attach to DX/VPN/VPC/peering with other TGW
<img width="1271" alt="image" src="https://github.com/user-attachments/assets/94211400-65f9-42ac-a33f-f0a486b64f3a" />
<img width="1251" alt="image" src="https://github.com/user-attachments/assets/3c323cf3-4716-4af8-818a-c15a0a4d9fc3" />
<img width="1235" alt="image" src="https://github.com/user-attachments/assets/f06bb225-db65-46f5-a34a-bd72b2aa32fd" />




# AWS VPC private link to SAAS application 


<img width="1175" alt="image" src="https://github.com/user-attachments/assets/4bc8b86f-3b2a-4316-9f11-029ff85840e4" />
<img width="1160" alt="image" src="https://github.com/user-attachments/assets/989a245d-6685-4d72-9e7f-7d80799c90d8" />
<img width="1168" alt="image" src="https://github.com/user-attachments/assets/e4d10da6-dd4b-4292-8ff2-494945115721" />
<img width="1161" alt="image" src="https://github.com/user-attachments/assets/cf53ec8d-852d-406e-8cf3-4609d40fbd3b" />
<img width="1672" alt="image" src="https://github.com/user-attachments/assets/480e2fcf-6676-4e3d-aadb-e2e337132e23" />
<img width="1609" alt="image" src="https://github.com/user-attachments/assets/b6e4a529-7b53-4354-b9bf-ac6889b15bac" />
<img width="1644" alt="image" src="https://github.com/user-attachments/assets/a57bcf47-c9d1-4a36-a5d5-17337a116c6f" />
<img width="1631" alt="image" src="https://github.com/user-attachments/assets/4dc0ac81-1cf3-49ec-b128-f45f597d1064" />
<img width="928" alt="image" src="https://github.com/user-attachments/assets/e7f2fa3a-dd65-49d6-9716-001c894ae3f8" />
<img width="944" alt="image" src="https://github.com/user-attachments/assets/ff477de5-0405-49f6-8629-777c425d83fb" />
<img width="919" alt="image" src="https://github.com/user-attachments/assets/a16d3749-54fa-4d64-82ed-ae807864dae1" />
<img width="939" alt="image" src="https://github.com/user-attachments/assets/52cd1a55-7733-49ea-8fd9-d410a8fcf87e" />
<img width="889" alt="image" src="https://github.com/user-attachments/assets/1e8fa1e8-9533-4ab1-aef0-75701b923d2d" />
<img width="931" alt="image" src="https://github.com/user-attachments/assets/2e78978d-6060-4a68-9326-4b3df8ec3a39" />
<img width="926" alt="image" src="https://github.com/user-attachments/assets/101b104d-0f6b-425a-8ceb-a2dc4767d39e" />
<img width="936" alt="image" src="https://github.com/user-attachments/assets/dc4a099b-1a55-4460-9b9e-062c9b79c59f" />
<img width="921" alt="image" src="https://github.com/user-attachments/assets/8d7e82d9-ace6-48ab-af34-119a4c32599c" />
<img width="904" alt="image" src="https://github.com/user-attachments/assets/fc4c22eb-c4d1-436e-a6f2-d76819b27549" />
<img width="926" alt="image" src="https://github.com/user-attachments/assets/738a8cfb-4acc-438b-9d5c-e04256cf1c78" />
<img width="935" alt="image" src="https://github.com/user-attachments/assets/5ab71531-f151-456a-9de7-01d1605ed6fa" />
<img width="930" alt="image" src="https://github.com/user-attachments/assets/8cb91bc1-1878-48fa-8ad7-3ae05c25c730" />
<img width="934" alt="image" src="https://github.com/user-attachments/assets/706f3b45-de61-40a9-ab6e-8ce98c53696d" />
<img width="939" alt="image" src="https://github.com/user-attachments/assets/c89ca706-5a70-4abd-8703-49154ddf48a9" />
<img width="1026" alt="image" src="https://github.com/user-attachments/assets/0a8bef38-1191-471a-98a0-0ed1f9932e81" />
<img width="1678" alt="image" src="https://github.com/user-attachments/assets/303d7247-d14e-4a39-b6bd-cb92696a3dce" />






<img width="807" alt="image" src="https://github.com/user-attachments/assets/805b2188-b13c-4194-b67d-ea87bc1aae0b" />
<img width="814" alt="image" src="https://github.com/user-attachments/assets/f00b80dc-0b04-4e01-a83e-e0eb12e87e76" />

<img width="924" alt="image" src="https://github.com/user-attachments/assets/6d945534-68fe-47b3-bb14-354ea7f921ed" />
<img width="932" alt="image" src="https://github.com/user-attachments/assets/1b762c54-4f37-4e58-9497-24a3a1eba6ac" />


![image](https://github.com/user-attachments/assets/7da46bd5-88dc-40cf-8b5e-8dcddf966d4d)
<img width="753" alt="image" src="https://github.com/user-attachments/assets/079a8971-89e6-41cb-be0f-53fce91fb14e" />

<img width="1166" alt="image" src="https://github.com/user-attachments/assets/90198dfb-2605-4d74-84d9-4bfd7ec88a3b" />
<img width="1069" alt="image" src="https://github.com/user-attachments/assets/f6ec339d-cf97-426a-b8de-a78fe4b43368" />


<img width="1675" alt="image" src="https://github.com/user-attachments/assets/f64e8806-5b26-49f0-929a-b5ff5a768f22" />
<img width="1652" alt="image" src="https://github.com/user-attachments/assets/c026bec6-f5f3-4ca4-8220-d39a69e98e69" />
<img width="1582" alt="image" src="https://github.com/user-attachments/assets/0a05870d-04f9-4e69-bb5f-9ab42afac071" />
<img width="1661" alt="image" src="https://github.com/user-attachments/assets/3c0b9bbe-b44e-4c66-81c4-5f90da262ed7" />


<img width="1158" alt="image" src="https://github.com/user-attachments/assets/a642817f-fb39-46ed-b7cc-49491c18afea" />
<img width="693" alt="image" src="https://github.com/user-attachments/assets/adebf9f4-9438-42d0-99b1-ce1072063d0e" />
<img width="1343" alt="image" src="https://github.com/user-attachments/assets/9dac2c99-9455-4327-86cb-30ebf52fc951" />
<img width="1332" alt="image" src="https://github.com/user-attachments/assets/646d2e63-c9bc-4703-bcff-b51bbf4215ab" />
<img width="1156" alt="image" src="https://github.com/user-attachments/assets/331729a7-e800-49d4-bc47-62f0c7d7f208" />
<img width="1153" alt="image" src="https://github.com/user-attachments/assets/87d69b39-9c41-4eac-b48c-423a8b1869c6" />

<img width="1122" alt="image" src="https://github.com/user-attachments/assets/78b956d1-9c4d-4d48-8f0f-31478dd67978" />

<img width="882" alt="image" src="https://github.com/user-attachments/assets/3ba8ea40-7477-4b69-8202-17cde816e24a" />
<img width="1137" alt="image" src="https://github.com/user-attachments/assets/5c79400b-1c7c-4dfd-ac26-7148de5c5b25" />



# AWS S3 encryption and object lock
SSE-S3  (Server-Side Encryption with Amazon S3 Managed Keys),CloudTrail Visibility: Invisible in CloudTrail. Since SSE-S3 uses AWS-owned keys that are managed entirely by S3, there are no events recorded in AWS CloudTrail related to key usage or encryption/decryption.

Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
<img width="661" alt="image" src="https://github.com/user-attachments/assets/c2dff21d-e9b3-492e-bbc7-22c1490aac3c">

<img width="723" alt="image" src="https://github.com/user-attachments/assets/25389de1-71f8-4994-bea5-7472f5f79208">
AWS-Managed Keys: Uses KMS keys managed by AWS (aws/s3 key) 
Customer-Managed Keys (CMKs): Allows users to bring their own KMS keys for more control.Visible in CloudTrail. When S3 uses AWS KMS for key management (via aws/s3 managed key or a customer-managed key), CloudTrail logs the following key-related events:
GenerateDataKey: A new data key is generated for encrypting the object.
Decrypt: The key is used to decrypt the data when accessing the object.
Encrypt (Optional): If explicitly triggered by API calls.


<img width="743" alt="image" src="https://github.com/user-attachments/assets/7f108ebc-4ac3-4762-ae34-4307b8c7e217">
<img width="1104" alt="image" src="https://github.com/user-attachments/assets/2e2ccdf5-0061-4ab8-ab61-8311677867f3">
<img width="681" alt="image" src="https://github.com/user-attachments/assets/8105bfff-3cee-4472-a2e3-a0ca4baf183e" />


Zero Trust Network (ZTN) is a cybersecurity framework that challenges the traditional security model of relying on a secure perimeter to protect internal networks. Instead of assuming that everything within the network is trustworthy, Zero Trust adopts a “never trust, always verify” approach. This model emphasizes continuous verification of all users, devices, and applications, regardless of their location within or outside the network


Route 53, AWS’s DNS service, also provides extra security measures to protect against attacks on the DNS protocol. First, you can leverage Route 53 Resolver DNS Firewall to filter outbound DNS requests from your own VPCs. Such requests go through Resolver to resolve domain names. If one of your workloads has been compromised by an attacker, they may want to exfiltrate data from your AWS environment by conducting a DNS lookup to a domain they control. DNS Firewall lets you monitor and control the domains that can be queried from your VPCs, so you can, for instance, allow access to only the domains you explicitly trust (allow-listing) or block queries to well-known untrustworthy domains and let all other queries through. DNS Firewall manages the lists of known bad domains, keeping them up to date, to make your life easier.

Second, you can enable DNSSEC validation on Route 53 Resolver in your VPCs. This will instruct Resolver to validate the cryptographic signature of the response you get upon a DNS lookup, thereby ensuring that the response was not tampered with. 

![Uploading image.png…]()



# AWS Lambda best practice (2024/11/15)

Monitor concurrency and execution usage metrics in AWS CloudWatch. Track results with Focus on on Throttles and ConcurrentExecutions metrics in Cloudwatch.
<img width="1436" alt="image" src="https://github.com/user-attachments/assets/e22504f3-0b48-47d1-ae0e-9760e4618868">

Monitor memory usage from Lambda Insights enhanced monitoring,Tweak memory and timeout settings as needed
<img width="1459" alt="image" src="https://github.com/user-attachments/assets/dfb6e45a-bac5-4ed1-be79-2ce601ffdd7e">
<img width="1701" alt="image" src="https://github.com/user-attachments/assets/be35638b-2c87-4af4-bd74-f2bc160438ab">
<img width="1484" alt="image" src="https://github.com/user-attachments/assets/17201348-43aa-42f3-b05f-294ae0bdb8a1">


Practical Steps to Reduce Lambda Cold Start Latency: 1  Choose a Lightweight Runtime
Use Interpreted Languages: Runtimes like Node.js, Python, or Go generally have shorter cold start times compared to compiled languages like Java or .NET Core.
2 Reduce Deployment Package Size,Eliminate Unused Dependencies and  Package Only What's Necessary. 3 Use Provisioned Concurrency,Enable Provisioned Concurrency: Specify the number of execution environments to be kept warm. Keeps a specific number of execution environments initialized and ready to handle requests, eliminating cold starts for those invocations.
<img width="1307" alt="image" src="https://github.com/user-attachments/assets/6c5fe13e-6f13-49b7-8aeb-1e449192ad77">

4 Increase Memory Allocation,More Memory Equals More CPU:Performance Boost: Allocating more memory also increases the CPU power available, potentially reducing cold start times.
5 Keep Functions Warm (Ping Functions) Scheduled Invocations: EventBridge Rules: Set up a rule to invoke the function periodically (e.g., every 5 minutes).
6 Avoid VPC Configuration When Possible,VPC Overhead: ENI Attachment: Lambda functions in a VPC require Elastic Network Interfaces, adding to cold start latency.
Alternatives: VPC Endpoints: If accessing AWS services, use VPC endpoints or keep the function outside the VPC if possible.

7 Setting Reserved concurrency based on requirement,  however If a Lambda function's reserved concurrency is reached, it cannot execute additional invocations until some of the currently running invocations complete and free up concurrency slots. 
<img width="1108" alt="image" src="https://github.com/user-attachments/assets/168f5652-a056-4257-8164-f42c8c0ff61f">
8 Allocate memory based on Cloudwatch log insight aviod resource allocation waste.
<img width="1487" alt="image" src="https://github.com/user-attachments/assets/8c956ca2-73d9-4ff6-8cc1-6ecd704f7516">

fields @timestamp, @message
| filter @message like /REPORT/
| parse @message "Duration: * ms\tBilled Duration: * ms\tMemory Size: * MB\tMax Memory Used: * MB" as duration, billedDuration, MemoryAllocated, MaxMemoryUsed
| display @timestamp, duration, billedDuration, MemoryAllocated, MaxMemoryUsed
| sort @MaxMemoryUsed desc
| limit 100

9 Setting SQS DLQ for lambda and cloudwatch alarm on the queue. It helps you monitor and get notified when events are sent to the DLQ, indicating that your Lambda function has encountered issues during processing.
<img width="768" alt="image" src="https://github.com/user-attachments/assets/7bbe83f0-5f1e-418c-b798-9cf557d26c60">
<img width="531" alt="image" src="https://github.com/user-attachments/assets/d1fd1cd8-bc67-426d-b028-8503dfbe7701">

10 Use lambda call ECS task. so it can surpass lambda task 15 minutes limitation. All related parameter such S3 bucket file can be pass to ECS task using containerOverrides overwrite parameter
<img width="838" alt="image" src="https://github.com/user-attachments/assets/bb48693e-b871-464f-8598-0ef740f70bd8">
https://github.com/xiongye77/aws_sysops_tasks/blob/main/lambda-call-ecs-task.py

<img width="908" alt="image" src="https://github.com/user-attachments/assets/6a8c01ac-00cd-4154-ba8b-b035d4756815">





# AWS ALB security (2024/11/15)
Add cloudfront prefix list as source security group for ALB so ALB can only be accessed by Cloudfront.
<img width="1659" alt="image" src="https://github.com/user-attachments/assets/b9204e49-9e8b-450b-8fc9-7ec882661504">
Add customer header and ALB only forward request to target group with proper header
<img width="763" alt="image" src="https://github.com/user-attachments/assets/ac6c2d0c-5bb8-4a7c-9d00-9e68409d4215">
<img width="718" alt="image" src="https://github.com/user-attachments/assets/1483f169-8788-4006-92f8-7d829eee8248">


# ECS and EKS service disconvery
<img width="828" alt="image" src="https://github.com/user-attachments/assets/b0a39cb8-a690-44e4-9bc0-db0e0b95a238">
<img width="907" alt="image" src="https://github.com/user-attachments/assets/6f68b011-10b1-415f-9309-dfc93f69ef2e">
<img width="904" alt="image" src="https://github.com/user-attachments/assets/3b504e97-abdb-4052-8e49-4546c0ad1ac8">

# ECS task definition access private repo 
<img width="1058" alt="image" src="https://github.com/user-attachments/assets/86d23519-bb11-462d-8e46-ac3ab87c52fb">
<img width="691" alt="image" src="https://github.com/user-attachments/assets/239aa590-2fdc-4c41-89a2-b59dcf249a73">


# AWS App Auto Scale
<img width="676" alt="image" src="https://github.com/user-attachments/assets/a5d97085-9d93-4f91-948d-b5e9f77fc733">
<img width="766" alt="image" src="https://github.com/user-attachments/assets/810ec649-39a3-4de9-b350-50291fd83985">
<img width="988" alt="image" src="https://github.com/user-attachments/assets/4e822d96-47f7-46d5-8edd-c58d77e02fd9">
https://github.com/xiongye77/terraform-carsales-test/blob/b3ce04fa0f57dfcdeedbf293818716de2658dca6/ecs-ec2-service.tf#L362



# AWS RDS Backup/Automatically Snapshot/PITR 
<img width="734" alt="image" src="https://github.com/user-attachments/assets/6da031e8-2514-49fa-b747-b777c7674283">
<img width="722" alt="image" src="https://github.com/user-attachments/assets/5948affa-6222-4a98-bf53-347c6fc29085">
<img width="1164" alt="image" src="https://github.com/user-attachments/assets/37595286-afd2-48cd-a4a3-350b28554b0c">
<img width="1088" alt="image" src="https://github.com/user-attachments/assets/b42fbfb0-8a54-4491-a702-33e73fc9ff2f">
<img width="1120" alt="image" src="https://github.com/user-attachments/assets/aa59741f-993f-4299-b50e-3bdf0513cdd3">



# Amazon OpenSearch 
<img width="911" alt="image" src="https://github.com/user-attachments/assets/5b6f2a96-7b8a-4702-b853-5402b8aa36bd">

<img width="916" alt="image" src="https://github.com/user-attachments/assets/cab73405-4df2-43bb-8159-adf7bca9bf1e">
<img width="907" alt="image" src="https://github.com/user-attachments/assets/d6774fe1-f3fc-4a1c-afed-a66a5fa71cee">
<img width="912" alt="image" src="https://github.com/user-attachments/assets/35ca4ccb-da89-4618-93c5-e3df3b31f778">
<img width="906" alt="image" src="https://github.com/user-attachments/assets/1df30634-defe-46a3-8658-c300bd8f77de">
<img width="904" alt="image" src="https://github.com/user-attachments/assets/8f535bb5-1e96-4ba0-96bd-835797260723">
<img width="912" alt="image" src="https://github.com/user-attachments/assets/1f5213ba-8523-445b-b6da-014f6058c63f">
<img width="905" alt="image" src="https://github.com/user-attachments/assets/76d22275-a847-4e05-9eb1-6c614f09c372">
<img width="906" alt="image" src="https://github.com/user-attachments/assets/0e3eff0a-e5df-47d7-b817-0b71893c074d">

# AWS EBS snapshot share cross account (2024/11/03)
if snapshot is not encrypted using CMK, it could not be shared account account 
<img width="1446" alt="image" src="https://github.com/user-attachments/assets/fabe9dbf-9dce-483b-9151-94b6826cc529">
<img width="1487" alt="image" src="https://github.com/user-attachments/assets/03d41051-d07e-472f-b5b0-bad66b3787ab">
<img width="1506" alt="image" src="https://github.com/user-attachments/assets/f37e4805-14e7-4ac5-b34a-75b13f131f91">
<img width="1639" alt="image" src="https://github.com/user-attachments/assets/7322931a-913e-43f4-8ce7-0496ad0fcf58">

Also need change CMK policy to allow target account to use it 
<img width="1424" alt="image" src="https://github.com/user-attachments/assets/6c2e3ae5-a20d-406c-8f41-3c550c234654">


# AWS EFS Security (encrytion in transit and encrypt in rest)
At Rest: Activate encryption during the creation of your EFS file system to protect data stored on disk. This utilizes AWS Key Management Service (KMS) for key management.
<img width="616" alt="image" src="https://github.com/user-attachments/assets/18f10dfa-24bc-4d71-b544-6d612e747fcf">

In Transit: Use Transport Layer Security (TLS) to encrypt data as it moves between clients and the EFS file system. This can be configured by mounting the file system with the appropriate options (-o tls)
To enforce security for data in transit on an Amazon EFS file system, you can use an EFS file system policy that requires all client connections to use encryption in transit. 
<img width="920" alt="image" src="https://github.com/user-attachments/assets/dbcfabb9-85da-45b1-8a74-c1395b1148d7">
<img width="1044" alt="image" src="https://github.com/user-attachments/assets/45743526-85e3-4239-9fee-eeae6c9d2ee1">

# Ingest Stream data into Snowflake/Redshift 

with Amazon Data Firehose

<img width="667" alt="image" src="https://github.com/user-attachments/assets/85da0166-8a46-4209-93f4-d55f925acc32">
<img width="665" alt="image" src="https://github.com/user-attachments/assets/86455835-0cf8-4635-bf52-bd25522867df">
<img width="820" alt="image" src="https://github.com/user-attachments/assets/3bf40ab8-fc43-4ae4-a21f-97cf4ad3cad7">


# Amazon EventBridge Pipes (2024/10/24)
The AWS::Pipes::Pipe resource enables you to connect a source to a target, with optional filtering and enrichment steps in between. This helps automate the flow of events from event producers to event consumers, facilitating event-driven application design.



<img width="1150" alt="image" src="https://github.com/user-attachments/assets/0dbd1e57-1242-4d35-8497-4cbf577306ac">
How It Works:
Event Source: The source of the events. This could be an AWS service like Amazon SQS, Amazon Kinesis, DynamoDB streams, or even an API Gateway.


Target: The service that receives the event, such as AWS Lambda, EventBridge, Step Functions, or other AWS services.


Filter: You can apply filters to the events, so only the events that meet certain criteria are passed on to the target.


Enrichment: You can enrich the event before sending it to the target, for example, by calling a Lambda function to add extra data.


<img width="733" alt="image" src="https://github.com/user-attachments/assets/4961e2c0-04a8-41b2-b416-d4d88ebb1b4c">

https://github.com/xiongye77/aws_sysops_tasks/blob/main/eventbridge-pipe.yaml
<img width="1126" alt="image" src="https://github.com/user-attachments/assets/149d3f05-cfa7-413d-a267-d0a2929085b6">

# Redshift Serverless monitor (2024/10/14)

Performance Monitoring
<img width="1710" alt="image" src="https://github.com/user-attachments/assets/e9080826-be9f-45ec-987b-74b9d943694e">
<img width="1726" alt="image" src="https://github.com/user-attachments/assets/742ddc1e-64f7-4897-9814-16e131cd8684">
Snapshot (manually and customer retention period) and Recovery Point (automatically and 24 hours retention period) 
<img width="1710" alt="image" src="https://github.com/user-attachments/assets/39653ba1-5f5c-4fbf-9a5f-154159406748">
<img width="592" alt="image" src="https://github.com/user-attachments/assets/03dbe8dd-ab0c-43a4-8865-7397e17ee6da">

Restore table from Snapshot
<img width="1446" alt="image" src="https://github.com/user-attachments/assets/bef4d446-22cf-46e6-95cd-9fa22472917d">

Restore to previous recovery point
<img width="503" alt="image" src="https://github.com/user-attachments/assets/c1a80d8d-9cb7-469a-9a21-dee3d39782d8">

Use GUI to load data from S3 bucket 
<img width="1721" alt="image" src="https://github.com/user-attachments/assets/c04eb215-3526-4cf2-92f1-f26b14e4170b">

Redshift Spectrum to scan S3 directly 
<img width="998" alt="image" src="https://github.com/user-attachments/assets/77e5a9fc-5074-437c-8003-47814b9457a4">

<img width="1013" alt="image" src="https://github.com/user-attachments/assets/db26292a-143b-4497-be7e-da8ee5ae18f7">



# AWS Step Function to pipeline file transformation and load to Redhshift  (2024/10/10)
https://github.com/xiongye77/aws_sysops_tasks/tree/main/statemachine

<img width="1687" alt="image" src="https://github.com/user-attachments/assets/67ec899b-1b0c-45e6-8bfa-79c709e3faf5">
<img width="1087" alt="image" src="https://github.com/user-attachments/assets/08ae8a58-4b46-4c31-8b48-64a6a28e64cc">
<img width="1460" alt="image" src="https://github.com/user-attachments/assets/d28acdee-09d6-4c81-9c6e-bdd6bed96c1d">

<img width="1372" alt="image" src="https://github.com/user-attachments/assets/03168c90-9946-4800-94d3-6ad288373ec5">
<img width="1448" alt="image" src="https://github.com/user-attachments/assets/df896308-a16c-4542-bf00-a43c800b929a">

verify converted parquet file schema using simple python code 
<img width="1718" alt="image" src="https://github.com/user-attachments/assets/bf095ea1-79f7-4321-bdb0-a8e45769b4e9">


# AWS Glue ETL job to change json to csv (2024/10/07)
<img width="839" alt="image" src="https://github.com/user-attachments/assets/ac1e75cd-60bc-41f5-9204-9d6d04b67a09">
Requested number of workers to 2 (minimum value) to save cost and Enable Job Marker to avoid unhandle duplicate files.

<img width="1383" alt="image" src="https://github.com/user-attachments/assets/5761cd01-47e1-4569-830e-961d12de9e09">
<img width="1727" alt="image" src="https://github.com/user-attachments/assets/291ac25b-6139-4872-9537-2e77b7519625">

https://github.com/xiongye77/aws_sysops_tasks/blob/main/flatten-json-csv.py
refer it 

<img width="1472" alt="image" src="https://github.com/user-attachments/assets/9f2d7f4c-51e1-4703-87aa-ecd38a44139a">

How Glue connect to private resource (RDS/Redshift) 
<img width="796" alt="image" src="https://github.com/user-attachments/assets/0d4a16c9-6945-43ec-9fb9-3a339a50dbff">

# AWS Cost Explorer with Amortized costs (2024/07/24) and AWS Compute Optimizer 
![image](https://github.com/user-attachments/assets/54746544-28a5-4c21-9f25-ecb179654a57)
![image](https://github.com/user-attachments/assets/7812ee7b-f448-40ab-b3ec-1895ea24dec9)
Amortizing is when you distribute one-time reservation costs across the billing period that is affected by that cost. Amortizing enables you to see your costs in accrual-based accounting as opposed to cash-based accounting.
<img width="1248" alt="image" src="https://github.com/user-attachments/assets/65683bd5-c835-42f3-aeec-fa163a376601">

AWS offers a range of compute services — EC2, ECS, Lambda, and more — with flexible configurations. However, determining the right amount of compute resources for your workloads can be challenging. Over-provisioning can be costly, while under-provisioning may lead to performance issues.
<img width="1659" alt="image" src="https://github.com/user-attachments/assets/1d9f1778-ddc0-4920-9188-65796f5aa557">
Compute Optimizer continuously analyses your resource usage and provides recommendations to optimise your compute allocations, including EC2 instance types and Lambda memory settings. By following these recommendations, you can significantly improve cost efficiency and performance.
# AWS Security Lake  (2024/08/04)
Security Lake automates the collection of security-related log and event data from AWS sources such as AWS CloudTrail, AWS Security Hub, AWS VPC Flow Logs, Amazon Route 53, AWS Lambda Execution and Amazon S3 data events while those from non AWS sources need their log format to be converted to a standard open-source schema called the Open Cybersecurity Schema Framework (OCSF). It is to be noted that many of the well-known security tools in the market generate their logs in OCSF schema and the number is increasing each day.
![image](https://github.com/user-attachments/assets/32d8f1b1-fd94-44d0-b5fd-a7be79af2522)

![image](https://github.com/user-attachments/assets/30bfe6e8-ad13-4cc3-a9b2-39953a9623d5)
![image](https://github.com/user-attachments/assets/e14300c7-efa5-4834-a4c1-ea3f520f0881)


# Trust advisor suggestions check. 

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

# WAF with OWASP top 10 (Open Web Application Security Project) (2024/04/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0905e7da-38bd-4d2d-9261-d9ca57759b07)

# Cross account cloudtrail gather to one dedicated S3 bucket under security review account 

![image](https://user-images.githubusercontent.com/36766101/159195015-f08b19f9-d6ef-472e-bc2e-a6795f1a0b3c.png)
![image](https://user-images.githubusercontent.com/36766101/159195104-66626a0d-9cd7-41c1-b348-bb906441930f.png)



# cloudfront access log check and S3 access log check (2023/07/25)
Cloudfront connect to origin web site always report 502 error, check cloudfront log use Athena. After check AWS document, it related to Cloudfront could not connect to origin. 
To fix this error, either have to change origin protocol policy from HTTPS to HTTP such that CloudFront does not use HTTPS while trying to connect to the origin rather uses HTTP. Alternatively, work with the origin to make sure that when CloudFront makes a request to the origin with SNI value of "aepcdp.carsales.com.au" it should respond with a certificate that either covers the origin domain name or the host header value that you will be forwarding.

Since we need ensure security in transit, so we have to work with Adobe on accept cloudfront https connection. 


the Viewer protocol policy still https only -> Viewer protocol policy determines the connection between the client/browser and CloudFront so that should not impact the website

![image](https://user-images.githubusercontent.com/36766101/157428045-9ba3dd09-7f93-49c9-85bd-6355afaf48a5.png)
![image](https://user-images.githubusercontent.com/36766101/157428243-2141416f-bcb7-4883-a48e-edb5b8034c8e.png)


Control origin request (When a viewer request to CloudFront results in a cache miss (the requested object is not cached at the edge location), CloudFront sends a request to the origin to retrieve the object. This is called an origin request)
Some information from the viewer request, such as URL query strings, HTTP headers, and cookies, is not included in the origin request by default. But you might want to receive some of this other information at the origin, for example to collect data for analytics or telemetry. You can use an origin request policy to control the information that’s included in an origin request.

![image](https://user-images.githubusercontent.com/36766101/157431965-b7544cd5-374f-486c-a7cf-663f09d4d675.png)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4342d02e-3d6b-4664-8a21-fcc1889ca57a)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5208dfd4-0c64-4d76-aca5-cd9d3d99b21d)


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


A user pool is a user directory in Amazon . With a user pool, your users can sign in to your web or mobile app through Amazon . Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f6d309fb-edce-40a7-a005-efdd5105a983)

# AWS Cognito User pool and Identity pool
![image](https://github.com/user-attachments/assets/2eb7f480-f83e-43ad-bcbd-64f8b7af3905)
![image](https://github.com/user-attachments/assets/49eba7a5-73cb-46bb-a6cf-ad0fe7632d33)
![image](https://github.com/user-attachments/assets/ee83dbcb-513a-458a-bd25-88332ea1d258)

![image](https://github.com/user-attachments/assets/de01f543-1f91-451b-9a5b-7b0c942a0ccb)

Amazon Cognito identity pools (federated identities) enable you to create unique identities for your users and federate them with identity providers. With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other AWS services. 
![image](https://github.com/user-attachments/assets/272aef25-f9f3-4eec-9331-b46857802b77)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a06b3cf2-a3ae-480e-83f5-6e7559400b95)
![image](https://github.com/user-attachments/assets/b518f41b-570a-4863-87ad-427aa5fa620a)
![image](https://github.com/user-attachments/assets/6aa572c9-e57f-46db-b1a8-68eada79ac2d)

![image](https://github.com/user-attachments/assets/8bbfeb59-a456-4bcf-bce1-8cc5ca62ab82)
![image](https://github.com/user-attachments/assets/03e411c6-4753-4e44-ac66-b3901fb18faa)



# Stream AWS Cloudwatch Logs to Amazon OpenSearch Service (successor to Amazon Elasticsearch Service)

![image](https://user-images.githubusercontent.com/36766101/191262883-ebe59164-2ca9-4d85-aa15-43243bf7136c.png)



# AWS Eventbrige
four components:Event source,Event bus,Rule,Target
![image](https://user-images.githubusercontent.com/36766101/191629505-d38ffef7-fbb0-43ed-93f1-546a59c672a4.png)




# AWS Guardguty Cross account security check and send security finding to slack through cloudwatch event.
![image](https://user-images.githubusercontent.com/36766101/191954018-ef6a7f45-b2d1-4891-bc92-1bf041e9eac5.png)
![image](https://user-images.githubusercontent.com/36766101/191954490-eb6d077e-a8b3-4ea6-8207-1bdc36237612.png)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cdec2015-63ba-4a82-826e-f38365eaa313)

we’re going to send an email notification every time GuardDuty finds a potential threat by creating an SNS topic, then creating an EventBridge rule that looks for GuardDuty findings, and pushing those events to SNS for the notification. (2024/04/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/8c8cbede-8759-4a63-a6de-7a4f838d16c8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/27582f24-d36e-4b75-a5bb-d1d87f413d0f)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a8b2ad67-79cb-4df4-98ba-3214f83e7869)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d344051e-9591-4048-8753-f9cf93fd5142)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c6014be1-0c63-4b47-b9b4-5cad05173de1)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/de03477c-cadf-4d0e-8c83-dc15d2388fe8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/64bdba7a-0b03-40e3-8a29-dfe1b975481a)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/8e5025ba-7551-4bcc-8a78-168ee10df517)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4b8b60b0-fec2-4c43-8c4e-87d0aa7164ec)

# Amazon Detective 
Amazon Detective is a service that helps you analyze and investigate the root cause of security findings or suspicious activity. Using data from AWS Cloudtrail logs, VPC flow logs and AWS GuardDuty data, Amazon Detective will collate, filter the collected security data and using AWS Security Hub, GuardDuty, integrated partner security products, machine learning and statistical analysis investigates the security findings to get to the root cause of the problem or suspicious activity.
![image](https://user-images.githubusercontent.com/36766101/232459258-fd6957e6-5839-4d32-bc76-c57eeb2785f1.png)

![image](https://user-images.githubusercontent.com/36766101/192092102-217c98f8-f5fe-4356-94d2-857619c990cf.png)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/852a1781-5fc7-49f0-9c85-afa76bd4e545)


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
As with the Send Fanout Event Notifications tutorial, we will use a fanout messaging pattern using Amazon SNS and Amazon Simple Queue Service (Amazon SQS) to decouple the website from the backend systems. To get the event notifications to the right backend system, you could create a separate topic for each type of quote request, then add message routing logic to your publisher. 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3eda45b7-80d1-438a-b2e1-0188b5c7bd37)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6642588b-afe5-4b01-a2f2-76dcb59ce42b)


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
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/dd1bf2c3-ca84-443a-9bff-8a0da0bdcdb0)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/49a2beda-d45f-454e-b868-62020fcfd3fb)

AWS Security Hub sends its findings to Trusted Advisor.

Detective is a service that helps you analyze and investigate the root cause of security findings or suspicious activity. Using data from AWS Cloudtrail logs, VPC flow logs and AWS GuardDuty data, Amazon Detective will collate, filter the collected security data and using AWS Security Hub, GuardDuty, integrated partner security products, machine learning and statistical analysis investigates the security findings to get to the root cause of the problem or suspicious activity.
![image](https://user-images.githubusercontent.com/36766101/232459470-6677d9ac-29f6-4bd2-a69a-f6ea9636922c.png)
![image](https://user-images.githubusercontent.com/36766101/232461021-7a3ceb3e-f8a0-457d-a16c-0ea4a711d6d0.png)

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
![image](https://user-images.githubusercontent.com/36766101/229387687-d8fbf3c3-388c-45d2-b816-f945f412f97f.png)

https://aws.amazon.com/blogs/security/how-to-visualize-multi-account-amazon-inspector-findings-with-amazon-elasticsearch-service/
https://controltower.aws-management.tools/security/guardutydetect-securityhubremediate/

# AWS Inspector findings and account scan settings (2024/04/08)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d73b2cf3-b837-4836-b813-8dd83a1de462)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/18964e98-119a-44bd-adf6-840147037eff)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/002311bd-d5d4-4af1-afcb-60e2ab258b80)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/39e2e538-f762-438a-9760-7caa6f8b6e2f)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c06f71c6-edd8-4f66-8112-e07a3fb0ae3c)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/43452657-c2ce-449a-a2e9-61c709640566)

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
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/edf81efa-b27a-409e-9299-0e7ba9e57264)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0d1450d2-f08a-464c-ba55-60b2b8dd03c9)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/819058eb-6873-412e-9165-6d2301653fca)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2a10d9ab-8446-4bc6-bc66-f06128896ac2)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4d6b4041-af0b-4476-8a87-e96f6c475935)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/03b8e14f-0e59-462f-846e-b996844c1fd1)



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

# AWS SG/NACL/WAF/Network Firewall  (2023/03/03)
![image](https://github.com/user-attachments/assets/fa0ed851-95d5-4aa7-99e1-df199c12a9cc)

![image](https://user-images.githubusercontent.com/36766101/222422994-cb623917-7c5e-499b-ad92-d13293a81e58.png)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/403dffae-c96c-444b-82f9-d60ea8f8215b)

![image](https://user-images.githubusercontent.com/36766101/222427971-685e311b-18e2-4b2c-a0cf-f94829f1ccaa.png)
![image](https://user-images.githubusercontent.com/36766101/222428291-6c77e656-2527-421e-8e7a-9cff8d5e3253.png)
![image](https://user-images.githubusercontent.com/36766101/222557503-f89e6d0f-c572-4434-b6c3-e97a6281e9b1.png)
![image](https://user-images.githubusercontent.com/36766101/222558410-40609756-80c9-4bef-9200-611f8da510d8.png)
![image](https://user-images.githubusercontent.com/36766101/233751392-7374302d-0ddd-4c47-9599-319976c83515.png)
![image](https://user-images.githubusercontent.com/36766101/233751444-e41db819-93a5-40ad-bc0a-5260d0b8fe3a.png)


# EC2 Reset passwords and SSH keys on EC2 instances (2023/03/10)
https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2reset.html#automation-ec2reset-how
![image](https://user-images.githubusercontent.com/36766101/224241045-de31ed2c-fa9d-4c7e-bf35-63358ba4e2d9.png)


# AWS VPC private link (VPC endpoint service) (2023/03/10)
![image](https://user-images.githubusercontent.com/36766101/224284676-742f2ed9-3ced-45de-af30-f20f891f3f52.png)
![image](https://github.com/user-attachments/assets/895aa1c5-3c97-467f-b9d4-2733113d18f5)

![image](https://github.com/user-attachments/assets/3afeadfa-b54b-4ec8-87f6-c312c7afaac7)

![image](https://user-images.githubusercontent.com/36766101/224284833-2d501ee2-19ea-4c74-b0f7-290594360d1c.png)


# AWS Cloudfront Signed URL and Signed Cookies (2023/10/29)
![image](https://user-images.githubusercontent.com/36766101/224848739-73fd58e6-9070-40d6-aaaf-8dbea351e7bc.png)
![image](https://user-images.githubusercontent.com/36766101/224286591-af58d25d-09ae-4790-a5f0-7412da619d27.png)
![image](https://user-images.githubusercontent.com/36766101/224287561-01b4b9f8-4e8c-4207-b387-8c01021fa078.png)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1e903219-1524-4f03-a2ef-0891380d9d6e)


# AWS Cloudfront OAI and OAC
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/32bd467e-4bec-494e-9e45-e42dd5315a8d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/df691758-ab6c-45d3-b2f8-e377398eddb3)

# AWS Firewall Manager and Network Firewall  (2024/04/09)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c19bcec3-b701-40df-afa9-02f6c5a15247)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6df52aa0-d6c3-4b68-b841-5f92e21f92b6)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/79bcdccf-939b-49b9-85f3-6519481d644b)

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

# AWS cloudshell public IP
![image](https://user-images.githubusercontent.com/36766101/226505432-02b7f245-58d4-4cc5-8bda-116bacbe3271.png)

# AWS lambda function url and monitor
https://aws.amazon.com/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices/
![image](https://user-images.githubusercontent.com/36766101/226512873-1cde2e7e-2ffc-4242-b659-44661e25c94a.png)

# AWS EFS enforce in-transit encryption for all clients or Multiple AZ consideration
![image](https://user-images.githubusercontent.com/36766101/226559375-5c2ef059-c7ea-4951-a988-7ce9e0060ddf.png)
![image](https://user-images.githubusercontent.com/36766101/226560553-cfe8e8e9-58e2-4335-8570-31ea484c9db3.png)


# AWS S3 inventory and Athena query inventory information (2023/07/25)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a3421352-3b5c-445b-aed4-907283302272)

![image](https://user-images.githubusercontent.com/36766101/226574397-47578676-8f1d-4152-8da2-080a23fd551e.png)
![image](https://user-images.githubusercontent.com/36766101/226574644-5e816036-d535-4823-9253-ae85f126ef45.png)
![image](https://user-images.githubusercontent.com/36766101/226574746-fb66a2b5-a1b1-4221-a61c-49c8c791b09e.png)


# AWS Config use managed rule to perform checks such as s3-bucket-server-side-encryption-enabled
![image](https://user-images.githubusercontent.com/36766101/226596418-7094d471-0927-4d63-b787-f9e11b61d008.png)


# RDS action item for upgrade and major version 
![image](https://user-images.githubusercontent.com/36766101/227433715-6856031d-237c-41d3-af81-c8718856f8ae.png)
![image](https://user-images.githubusercontent.com/36766101/227433745-31bb8dd0-8d1f-409b-b094-fda754f0f685.png)
![image](https://user-images.githubusercontent.com/36766101/227435477-17bc978a-b213-4b0d-b2bf-1648ee4f0308.png)
![image](https://user-images.githubusercontent.com/36766101/227435579-bc1b874e-c71d-44de-86e6-589df7900778.png)
![image](https://user-images.githubusercontent.com/36766101/227463267-51188ae7-60b2-4cb9-abd5-b3bd5001aa65.png)

# RDS export to S3 , a new role for service export.rds.amazonaws.com
![image](https://user-images.githubusercontent.com/36766101/227468640-59542315-fa39-4350-83b3-8671eed9cdfb.png)
![image](https://user-images.githubusercontent.com/36766101/227476332-2fa09f9d-316d-442c-918d-4064f41886c6.png)
![image](https://user-images.githubusercontent.com/36766101/227477267-a99f3cf4-1f25-42ed-9272-a8bafbd32a6d.png)

# AWS Config compliance check for ACM
![image](https://user-images.githubusercontent.com/36766101/233748854-c73f77c3-31ec-4616-a911-75028fae88cf.png)
![image](https://user-images.githubusercontent.com/36766101/233750856-777f5461-6f1d-4e65-b9c4-10c874ac3b43.png)

# AWS cloudwatch log contributor insights for AWS WAF log (2024/03/10)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f29e5cd2-f413-48e2-a75d-62520b23f7e0)

# AWS Cloudwatch log Contributor Insights for VPC flow log
![image](https://user-images.githubusercontent.com/36766101/233754175-c66dd621-f935-4d07-8c26-ed61f3f4dfe0.png)
![image](https://user-images.githubusercontent.com/36766101/233754220-50aa9cbb-f43f-4fba-9ee2-6b1cb68e3bd3.png)
![image](https://user-images.githubusercontent.com/36766101/233754257-560272f4-831f-4926-882e-03e0417f7dca.png)
![image](https://user-images.githubusercontent.com/36766101/233754416-b934423f-52ea-4778-b499-5f351dd8ad09.png)

# AWS network Reachability Analyzer 2023/04/22
![image](https://user-images.githubusercontent.com/36766101/233769601-f78bb7ae-3823-4e07-a5b0-5d31a5e78ff3.png)
![image](https://user-images.githubusercontent.com/36766101/233769729-a90e5420-c899-44ce-8587-582c31729bb4.png)

# AWS VPC Endpoint
![image](https://user-images.githubusercontent.com/36766101/233873185-e599115b-436d-4d66-a09c-a905d4a1e999.png)
![image](https://user-images.githubusercontent.com/36766101/233873211-1174f646-0c49-4d49-9153-a810619391ae.png)
![image](https://user-images.githubusercontent.com/36766101/233876076-3a5e8d2e-4a39-4b9e-98da-41935d080d1c.png)
vpc endpoint policy and S3 bucket policy works together.
![image](https://user-images.githubusercontent.com/36766101/233882792-2a423194-be6a-4133-a25e-3b3a13400f54.png)
![image](https://user-images.githubusercontent.com/36766101/233885113-a7061de1-1ba7-489e-a58a-27ed8cf3d956.png)
![image](https://user-images.githubusercontent.com/36766101/233885399-1de336bb-63af-43d6-a03f-bb21f08ef28b.png)

# AWS S3 bucket key 2023/04/24
without S3 bucket key
![image](https://user-images.githubusercontent.com/36766101/233911107-ea9a4876-d6ef-4123-a97d-3765bfad5df4.png)
with S3 bucket key
![image](https://user-images.githubusercontent.com/36766101/233911265-9af09042-1e3a-4964-a5da-3fe32f0ac41b.png)


# AWS Maice 2023/04/24
![image](https://user-images.githubusercontent.com/36766101/233981561-cdb31de4-8c61-447d-9347-e67d8372f086.png)
![image](https://user-images.githubusercontent.com/36766101/233997917-e087c52b-d907-40da-81b8-f36710cd75ed.png)

![image](https://user-images.githubusercontent.com/36766101/233996268-039f0c21-6d01-4e73-a260-6712a83da4ff.png)
![image](https://user-images.githubusercontent.com/36766101/233996750-acc264ed-e06b-4994-8c28-e67dc8612365.png)


# AWS RDS proxy 
![image](https://user-images.githubusercontent.com/36766101/234430374-18475afa-1582-408c-9793-47b24bcb15c8.png)

# AWS Cloudwatch Log subscription
![image](https://user-images.githubusercontent.com/36766101/234446916-594ba469-43fd-4bec-8678-a754288c8d02.png)
![image](https://user-images.githubusercontent.com/36766101/234447120-f5eab118-f5fd-4950-8d4c-f9287e4756da.png)

# AWS Glue Schema Registry
AWS Glue Schema Registry is a fully managed service that provides a central schema repository for organizing, validating, and tracking the evolution of your data schemas. It enables you to store, manage, and discover schemas for your data in a single, centralized location.
With AWS Glue Schema Registry, you can define and register schemas for your data in the registry. You can then use these schemas to validate the data being ingested into your streaming applications, ensuring that the data conforms to the expected structure and format.

![image](https://user-images.githubusercontent.com/36766101/235057831-3126d32d-1a0a-40d3-92ef-67d7c078fd34.png)


# AWS Firehose deliver stream parition data based on date
![image](https://user-images.githubusercontent.com/36766101/235819579-3e899d36-300a-4b05-9bbf-585c2121fcfa.png)
![image](https://user-images.githubusercontent.com/36766101/236347194-a55efb11-0ace-400c-880e-f85731577af3.png)


# AWS S3 replication (2023/05/08)
Make sure check replication status 
![image](https://user-images.githubusercontent.com/36766101/236732578-4d0904ef-fd8b-4f96-9083-2b4469934bd2.png)
![image](https://user-images.githubusercontent.com/36766101/236956208-47b73aed-31ac-49da-a2c1-601ecb343f77.png)
Make sure Prefix is correct, there is no / at the begin of Prefix
![image](https://user-images.githubusercontent.com/36766101/236732656-dc82f1cf-aaa9-473a-8c51-0c7c6a9cca9b.png)
Since source bucket and destination bucket use different kms key to encryption,make sure to use correct kms key 
![image](https://user-images.githubusercontent.com/36766101/236733367-92b28027-c994-4c2d-b280-8893b916fe71.png)
Make sure use IAM role with proper policy, it will involve use kms keys 
https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html
Use Cloudtrail S3 data event to monitor all write operations to replication target bucket or use S3 access logging
![image](https://user-images.githubusercontent.com/36766101/236764518-1c94c77b-95f2-4f7c-b5fb-04a60e51c3f1.png)
![image](https://user-images.githubusercontent.com/36766101/236765444-1bc92b64-cabb-4c6c-8575-7b5ef2a07add.png)
![image](https://user-images.githubusercontent.com/36766101/236960638-40fdeebd-d6c2-4dc8-9887-3e5b66f62316.png)


# AWS lambda function DLQ (2023/05/11)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d22cd597-f4d6-4bba-91e8-c0dd1c89cc53)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/be43b739-55f1-4359-8f10-45339cf5262d)


# AWS S3 mutiple part upload (2023/05/11)
https://repost.aws/knowledge-center/s3-multipart-upload-cli
time aws s3 cp emailsentperjourney-1.csv s3://digital-data-eng-storage-integration-prod-ishz/  --sse-kms-key-id arn:aws:kms:us-east-1:333186395126:key/mrk-cc4c9049c0804590b0562bd38f6206a2 --sse aws:kms
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/25b99ee5-c296-4a1c-9477-458b86fec1e1)
https://github.com/xiongye77/aws_sysops_tasks/blob/main/multipleupload.py

# AWS Redis and Memcached for ElastiCache
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/22f78c19-ab23-48e4-93ac-205e3ab66828)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/aeb58ae9-0f9a-44c7-9ad0-84c1daa2da3a)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e8201802-d8d7-485a-b1a4-5a1512719d88)


# AWS S3 bucket file replication status (2023/06/01)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7dd73119-1a86-43cb-ae8b-d261764f2585)


# RDS proxy multiple client connections single database connection (2023/06/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e49ecfa0-8e81-4b2c-a09d-c5967524fa01)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ed000383-f7a9-4a3b-83c9-db45de979c77)

# RDS snapshot upgrade, upgrade to new database version (2023/06/08)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/40ce360d-a23f-4ebc-8206-69013ad18f36)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4cb413db-d146-4f9d-8e94-b47f08b4584d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d484b5ed-f3e3-4772-877f-1576212f8244)


# RDS migrate to Aurora (2023/06/08)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3e6f09c4-4a54-4706-b0e5-33d5f958ea7a)


# AWS cloudwatch cost analysis (2023/06/09)
APS2-DataProcessing-Bytes related to log entries put to cloudwatch log groups, query cloudwatch incomingbytes metric and sort with log group have most incoming bytes.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2d1db1b2-781f-4371-9d45-248c504100a8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6aaa56fd-2605-405f-a176-2c9a4efa7237)

# AWS S3 encryption and object level access control using ACL and bucket level access coontrol using bucket policy (2023/06/13)
Encryption at transit(https/ssl/tls)


Encryption at rest: Service side encryption

SSE-S3 S3 managed key /SSE-KMS (Customer Managed Key cross account key/AWS Managed Key)/SSE-C customer provided key

Encryption at rest: Client side encryption

Client encrypted before upload


CORS access bucket contents from another bucket , store different contents in different buckets
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5541bbbd-652b-4f5d-a3db-6865f5786a8d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5e377a45-3ce9-4ecb-bd58-4817c64d1302)




# AWS Sagemaker Canvas (2023/09/23)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/47c9670f-7859-41f4-9936-381c9b615f34)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cc2be801-1a1e-40ca-9ea8-286804ed9cba)

Using SageMaker Canvas, business analysts can now build ML models and generate predictions on their own by importing any dataset from their Snowflake accounts and defining the model they would like to train in a few clicks. We can also generate single and batch predictions and maintain different versions of the model without writing a single line of code.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2028da33-501c-440a-96be-80f0ea140453)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/20dd59b8-9b25-45e3-a34e-d2d5024d44be)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/00ee3fd4-c635-40a7-8d09-fe9ce93c38f1)


# Kafka schema registry
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9f1cbd0c-b1e1-4d68-8078-fdf1a4ed2954)



# AWS DynamoDB security (2023/06/23)
different tables use different CMK keys so control users access
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/09e03215-add3-4b9c-839b-f1d6925c20bb)
# AWS DynamoDB provisioned capacity with autoscale vs on-demand capacity  (2024/01/28)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/85aa9f99-60ca-445c-8c12-5edbda1a65c8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/924ed675-54bd-4f55-a98c-b7af3e23615e)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4bfc2d24-f337-4d26-af5d-7beeefb69653)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/12ef5020-c8f1-4f60-9655-aa579a132315)

With provisioned capacity you can also use auto scaling to automatically adjust your table’s capacity based on the specified utilization rate to ensure application performance, and also to potentially reduce costs. To configure auto scaling in DynamoDB, set the minimum and maximum levels of read and write capacity in addition to the target utilization percentage.


# AWS DynamoDB local secondary index /global secondary index  
Secondary index allow efficient access to data with attributes other than the primary key.
Local secondary index: An index that has the same partition key as the base table, but a different sort key. Local secondary index can only be created when create the table.
Global secondary index — An index with a partition key and a sort key that can be different from those on the base table.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/58da0454-6218-44ef-b834-627d47a20ba6)

# AWS DynamoDB stream to Kinesis data stream 
# AWS DynamoDB transaction
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/b397c7c7-0ca7-4951-bd8f-837c508abc86)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9f295555-1b0a-49e2-9e21-19cb5f6c9f1a)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/beb235bf-0422-4eca-b8dd-e54fe7c06f18)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/bac71bbd-12a6-40d1-83c1-d5956598a770)

# AWS DynamoDB stream
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1a8268b5-650e-493a-b841-a04dbbd40686)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/766214fb-c1b9-4add-9919-e73f2acf80bd)



# AWS S3 object lock and MFA delete (2023/06/25)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/373341f9-071e-445c-9bea-2af6b7ab44a7)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/86177581-1f62-411d-a04b-322570ac63fc)

could not be handled on S3 console only available on commandline
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6dd19833-b2c8-481c-b9f4-1286bdf16c31)


![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/74c91f74-3a75-4534-a676-b3c856248342)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4e4d472d-0010-4bff-8cbc-19e38cef3954)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/93d83f2d-690e-4824-99f4-fd33703d966b)


# AWS S3 replication,source/destination bucket with different CMK
Make sure prefix is correct without additional / at first, Make sure replication IAM role with permissions. For those failed replicated objects use S3 batch to replicate them again.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html


# AWS Firewall Manager (2023/07/13)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/43145c0a-9fff-40c7-8716-c6429f706a03)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7897e8f9-ff9f-4cf8-9e38-b28869efdf73)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4157437c-8baa-46f4-84b5-31434938f139)


# AWS API GW with Cognito User Pools & Cognito Authorizer
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/080af6d3-3733-4215-95b3-ff49a421b155)


# AWS Cognito Custom domain (2023/07/18) and ALB integration
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/307972d1-10a6-4a79-b887-2823b4649ba0)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/54075c17-4849-4f52-886d-d6e546b0a927)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a56c03dc-ac44-4575-a437-00646269c742)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ab3f2697-0615-4bd0-ad10-db16bdef4942)

# AWS Config Automated Remediation with SSM (2024/04/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a3ee77db-7529-484c-a80a-7343d03c46e1)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2cdfd387-391f-4329-b7e3-52b94ad2bbe4)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f9762b6d-35aa-4c45-b75d-ea5e7720d31e)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/07b20893-c946-4313-aadd-01113dea3a4b)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/599f96fe-89dc-4b9e-bdea-cc3b2043b0e5)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1f78b221-87b2-4f3f-97ba-36bf3762b957)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7605674b-948b-4632-b4ed-3b87997a2bf0)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9c2a1428-4639-4324-a470-ee2d9d7e1215)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3ad9eef8-9042-40a0-a1a9-6adaffe7a39a)

# AWS config to track changes,figure out which component changes cause application issue(2023/07/25)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/75eaa224-eb5e-4f61-a48b-252acbbff4c2)

# AWS Config Aggregator for Multiple Accounts (2024/07/23)
![image](https://github.com/user-attachments/assets/fddc038d-0634-453e-87a9-51362ff72f3b)

# AWS S3 access point 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/66a05648-f966-46b1-b40c-88ea046b0a12)
With S3 Access Points, we can create unique access control policies for each access point to easily control access to shared datasets. Need IAM Role/S3 Bucket Policy/S3 Access Point Policy
IAM Role
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a065f911-fade-49bd-9bc6-a136688717e8)
S3 Bucket Policy
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/91dc76bc-49ea-4835-9993-2d632853f42f)
S3 Access Point Policy
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/10f96583-9905-4229-88bd-babdff49e1d5)



# AWS S3 inventory used as S3 batch job source (2023/08/02)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/da3a1b60-9a53-42aa-8e8f-49a62f247d70)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/89ebb7ad-9d27-4c86-89f7-7ab77afa0af9)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e81d7066-7e9e-4f1a-9380-0ad406d54324)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/55149bb8-5e8d-45c6-b7be-69bfd041a5a9)

# AWS S3 SSE-S3 and SSE-CMK and use bucket policy to deny non-https traffic
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/8219b716-afa8-4914-9d7d-735b6aba7a20)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6d77c48f-1787-492e-a999-cc92c0d7c72d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cc430ba1-74ec-4932-81a0-e4a9bd801050)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/eb258904-acf5-46d0-9a20-c5a1f2a44dec)



# AWS MicroService Communication
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/10c558c1-1c93-4db9-a90a-958e6c40e895)

# AWS Network topology 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/01d09a4e-ec5a-4878-8ecf-174094f4cb43)

# AWS MSK
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/767fe7b1-09e9-4506-8cfc-109eea143e31)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3f685921-9471-4a45-9969-6877991b947f)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/436b0f96-b725-4c61-a041-96ccadd523f9)


# AWS Glue/EMR
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4c72bcb0-0747-41bd-85af-8c9058a7cf18)


# Amazon Managed Service for Apache Flink Renamed from Amazon Kinesis Data Analytics
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0c0b71d8-bb02-4732-9b3c-ade08bb59e86)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/35680d00-4ce3-4995-ab73-0aa7e950ec09)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2668ad89-0fb3-40b3-b4b1-05934c42d985)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0832d546-eab9-4a66-a955-cf22e7b3dfc8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9aea9195-0ed3-42ae-93fc-242577bd1734)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/68975713-9e2b-4c0d-8dd3-e2f90801e224)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/df4af2f0-083c-40b7-8b0f-9b20e6161453)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/a144227e-9750-423c-aaf6-6800e627744b)
![image](https://github.com/user-attachments/assets/00b765af-8d4a-4bca-aae7-6572eb52b481)


# AWS launch template repalce launch configuration and instance refresh 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c6f78a50-0d0a-431a-99c6-f2be94d6a477)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7689cf17-8fcd-4839-9343-83ff0874d77d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ed22bf9b-c079-4d45-a42a-eb86b6d6b67a)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4d20d9e6-c4c7-4984-80ea-664eb1d37983)


# AWS DMS/SCT 

Create DMS and Create source/target endpoint
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4608731e-17f0-4a44-abd6-dd4d25b49313)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/775ecdbf-72bd-486c-a239-3bbf93798068)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d8fb6d27-b9be-4ce8-8aff-4b603f98122d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ae60a93e-16f9-490c-993a-28748aa13fc1)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/62308236-4844-4337-a99a-b486d1e5d18a)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ac68ae87-27bc-4db2-8cde-98f41368a32a)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/28fa7bbc-f10b-4d25-8920-9b623f6e9814)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/351d7c34-7156-4a42-aa4a-a7c6c6cb040d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0416ecdc-d121-47d9-935e-4eb5a5e36a90)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/70d91ad1-0c4b-4560-bb12-5a65ae6cdc0a)


# AWS Bedrock Generative AI
Amazon Bedrock is a serverless offering where a lot of the grunt work with setting up training and hosting LLMs (Large Language Models (LLMs)) is abstracted out. Fine-Tuning is a specific feature within Amazon Bedrock.

Large Language Models (LLMs) refer to advanced artificial intelligence systems designed to understand and generate human-like text. These models are trained on vast amounts of data, enabling them to grasp complex patterns, comprehend language nuances, and generate coherent responses. LLMs have the capability to perform various language-related tasks, including language translation, text completion, summarization, and even engaging in conversational interactions. GPT is an example of LLM.


LangChain is an open-source framework designed to facilitate the development of applications powered by large language models (LLMs). It offers a suite of tools, components, and interfaces that simplify the construction of LLM-centric applications. 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c8bac04c-ad48-4971-a862-1c55d6088577)

https://github.com/xiongye77/serverless-bedrock-chat



# AWS API GW Cognito Authorizor (2024/03/05)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/973e6f3c-c322-449e-88fd-c1376b316471)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/98cd14eb-4576-447e-8532-fd8b39fa100c)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/fda34267-ff8a-4271-a993-a8ab4e637e0c)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/b301b8f3-e29c-4519-8286-f44fa98162f3)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4f9ce787-d280-486f-b390-19f0e8dee08f)

# AWS API GW Lambda Authorizor (2024/04/16)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7870819e-e202-4c8d-87dd-b601e5d61067)

https://github.com/xiongye77/api_gateway_lambda_dynamodb/blob/main/cloudformation.yaml

# AWS EvenrBridge monitor RDS event 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4a26cbcf-2ad7-42a7-8272-14e9c561421c)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/19d7c134-c5bf-4192-85e8-db20f7bb7f48)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9e8885ce-c466-428e-83e7-301ab2bc0c89)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d1adaf72-28d6-4d79-a3d0-af59c56c52cc)


# AWS Cloudtrail Insight Event and Cloudtrail Lake (2024/04/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0a389f86-6905-4ba9-b1a7-f5b35f6fd4a0)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3b3792e0-8728-43f7-aaa7-88afad3026aa)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/001fabd1-96a4-407d-8fd7-5a1fb80d1e55)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d1121a5f-f22f-45bf-ba93-ceb98285190d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4f3f7083-d63a-4167-add0-ba5663a5cb1b)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cbd09818-d187-444c-92a0-1ef205c04367)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e8bb0c25-6dd2-407a-9a10-518674797fad)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cf8aa1e4-c7f0-4101-8416-834a0f6629f6)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1703ea4a-5b44-47e4-b232-df5b88b8a0ab)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cb091724-6dd5-4e59-b82e-8b2b666ff944)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9a9c13af-588c-4605-abb2-919423dfd30b)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ebc20dcf-b656-40f7-92e5-fe029d046464)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/906a54d9-2cbd-4617-a5ab-c3a7f9a6db57)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/3067d5b5-b67d-43a6-89af-995bf120541e)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6e178e0e-61be-4877-b085-7563fb99fd35)
![image](https://github.com/user-attachments/assets/e08c03f8-49d9-4abf-ae1c-e7c0a16ab5c9)
![image](https://github.com/user-attachments/assets/bb0f99a5-ea76-4259-a04e-102b23103cb9)




# AWS Cloudtrail Security Control
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/83c136b0-cad1-4a08-a5f4-43e698a55fa0)

# AWS cloudformation check statck output 
aws cloudformation describe-stacks --stack-name YOUR_STACK_NAME  --query 'Stacks[].Outputs' --output json | jq '.[]'

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/01b3b735-3d08-4a40-93c5-1b1b9f533d29)

aws configure --profile/aws sts get-caller-identity --profile/aws sts get-access-key-info --access-key-id AKIAW7NLVZMHQ4IO2CRG
aws configure list/aws iam update-access-key --user-name username --access-key-id access_key_id --status Inactive/ aws iam list-access-keys --user-name  username 

# AWS cloudtrail Lake query (2024/04/07)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/d200c461-65cf-4bda-84e5-1c268293a915)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/cdafe2e5-f002-45a7-80a2-68ca173c40e6)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/fcf43233-9bb3-459b-98a5-f8904d51575d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/59f5efe8-64ed-40ba-8629-c89c79ac6fd5)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6a09c97c-2781-44d8-b3fa-76b24cd76920)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/aad3a0a5-f049-43b1-94e3-4c705ac4e91b)

# AWS IAM Identity Center
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/8a8e7aec-93a5-4dd8-9994-f000b74ea69a)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/533802b6-363a-4c81-bfe4-b150f61c0dad)


![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e261d907-98b6-45c0-91d4-e917ca213c67)

# AWS SSM Maintenance Windows (2024/04/11)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/e522648c-175f-48ec-8def-f77b0d3329a5)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4f7f5bc1-4487-4b8d-8b77-22c7310eac9a)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/318509f7-67d4-4412-88b2-342ec333e0ae)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/ac588ad5-0f26-4698-a258-4a0eadf3666c)

# AWS KMS aws managed key vs customer managed key
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/738e1a84-b550-4819-b344-bd9c17c13a30)


# AWS VPC Lattice architecture patterns and best practices  (2024/05/20)
Amazon VPC Lattice is an application networking service that simplifies connecting, securing, and monitoring service-to-service communication. You can use VPC Lattice to facilitate cross-account and cross-VPC connectivity, as well as application layer load balancing for your workloads in a consistent way regardless of the underlying compute type—instances, containers, and serverless. In this session, get a general overview of VPC Lattice, learn about the latest features and functionality, discover pro tips and tricks to adopt best practices, and explore top architecture patterns organizations use to simplify application connectivity, security, and load balancing.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/15639232-c2ed-4a0b-8d4f-955fba3af6c2)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9f5ba77a-c4b8-46d3-8e54-d5b600d51e99)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/b617b9d7-8f7b-4172-b74a-03680d4da22d)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/bd5d8a38-b5f6-4f0f-9183-5805204dba2f)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5b91c265-7dc0-47eb-8aa1-0db7254d7ac6)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9dc40210-b4d0-4ef5-94af-6b1f7ea14760)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1e00f3d5-ed9b-4bfe-94f7-35dd6d8f0fa8)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/9eaab303-259c-48ab-be49-f550ebdf5536)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/7bfe486c-5c2f-4a01-a013-7a871fd4c873)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/240ed91b-6d5e-4871-a857-1ff461c8dd63)


# AWS Glue Bookmarks  (2024/06/10)
AWS Glue Job Bookmarks help Glue maintain state information of the ETL job and helps process new data when rerunning on a scheduled interval, preventing the reprocess of old data.In a nutshell, Job bookmarks are used by AWS Glue jobs to process incremental data since the last job run, avoiding duplicate processing.The AWS Glue ETL job is triggered using Glue ETL trigger. As AWS Glue job bookmark is enabled, it processes the incremental data since the last successful run. For S3 input sources, AWS Glue job bookmarks check the last modified time of the objects to verify which objects need to be reprocessed. If input source data has been modified since last job run, the files are reprocessed when the job is run again.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/44fa8287-86cb-4e4f-95da-635541b0ddcd)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c46fd62b-f1d6-4902-982b-876b72ff4103)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5e017223-a18f-4078-892d-84a2cbcbaf81)


# AWS Glue crawler and job 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/00adf49d-9fa7-40da-be10-c4467e14cabf)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f83e78d3-0a04-4a23-a563-f67b3aab618c)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/03653de6-a659-4d3e-af6e-02e4d872b840)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/5780048d-0be9-43cd-86ea-f6188c8ea824)

AWS Glue Crawlers and Jobs serve distinct but complementary roles within the AWS Glue ecosystem. Crawlers are used primarily for discovering data schemas and updating the Glue Data Catalog, while Jobs are used for executing ETL processes to transform and move data


# AWS Cloudtrail lake (2024/06/20) enable Lake query federation
When you enable Lake query federation, CloudTrail creates a managed database named aws:cloudtrail (if the database doesn't already exist) and a managed federated table in the AWS Glue Data Catalog. The event data store ID is used for the table name. CloudTrail registers the federation role ARN and event data store in AWS Lake Formation, the service responsible for allowing fine-grained access control of the federated resources in the AWS Glue Data Catalog.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/26dc6c62-80ac-428e-8018-74e78fae58d0)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/0480ecfd-dd77-4794-8e24-a1cf423b0a19)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/4e0e698b-3856-4973-926d-758f199177f5)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/55436d02-d9e9-47f3-8624-4cc952817820)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/feee7e43-68d3-476a-918f-93661ad6560e)


# AWS speak/hub network   (2024/06/23)
We will create central ingress and egress using AWS Network Firewall and Transit Gateway. This will use a hub and spoke model where the networking account TGW and Network Firewall are set as the hub, and any other AWS account like development, production, or Staging account would be its spokes.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/6eb84536-7f4a-48d8-b709-a60cae203d25)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/be1fee75-1c75-4751-be25-0817b4377853)
Hub and spoke model
All traffic in and out of our networks flows through the Threat Protection Zone (TPZ). There are a small handful of TPZs, but many networks that they serve. This is why we refer to this design as the hub and spoke model. The hub is the TPZ, and the spokes are all the VPCs where the applications live. The TPZ has devices in it that scan the traffic in and out of the spoke VPCs. Traffic can be split into three main types: Ingress, Egress, and Cross-Account.

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2aac5971-b901-4ca8-b23b-d1383e734aea)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/672adacb-1b29-4d9c-933d-7cafe383fa77)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/446590b5-40c5-40b6-b131-b251dd27f199)

Having a central ingress and egress lets you know where your data is going and where your data is coming from.
The networking account is a DMZ (demilitarized zone), which almost all security frameworks such as NIST, HITRUST, SOC2, and more ask for DMZ.
No IGWs (Internet Gateways) and NATs ( Network Address Translation) in all the spoke accounts prevent data exfiltration.
Provide good insights into how much data is going in or out of the environment, allowing us to put CloudWatch alarms for data exfiltration.
Separation of accounts allows you to separate duties between networking people and DevOps folks.


# AWS WAF VS Network Firewall (2024/06/23)
AWS WAF
AWS WAF is a web application firewall that helps protect web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources.

Key Features of AWS WAF:
Customizable Web Security Rules: AWS WAF allows you to create custom rules to block common attack patterns, such as SQL injection or cross-site scripting, and rules that are specific to your application.
Real-Time Visibility: Offers near real-time metrics and logs of web traffic, providing insights into traffic patterns and potential threats.
Integration with AWS Services: Seamlessly integrates with services like Amazon CloudFront, Amazon API Gateway, AWS AppSync, and Application Load Balancer.
Managed Rule Groups: AWS provides managed rules, maintained and updated by AWS, to protect against common threats.
Rate-Based Rules: Capable of blocking IP addresses that exceed a certain threshold of requests in a specified time period, helping mitigate DDoS attacks.

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/c96c999f-c08d-4535-826f-8f2823fb20ba)

AWS Network Firewall
AWS Network Firewall is a managed service that provides network protections at the VPC level. It’s designed to protect AWS Virtual Private Cloud (VPC) resources.

Key Features of AWS Network Firewall:
Stateful Inspection: Provides stateful inspection of traffic at the VPC level, allowing it to monitor and filter outbound, inbound, and east-west (internal) traffic.
Intrusion Prevention System (IPS): Includes an intrusion prevention system to detect and take action against attacks.
Web Filtering: Offers domain and URL filtering to block access to malicious sites or enforce company policies.
Customizable Rules Engine: Allows the creation of complex rule sets for network traffic filtering based on various factors like IP, port, protocol, and pattern matching.
Integration with AWS Services: Integrates with AWS services like AWS Transit Gateway and VPC to provide a centralized firewall solution across multiple VPCs.



# AWS Global Accelerator
AWS Global Accelerator is a networking service that optimizes the delivery of internet traffic to applications hosted on AWS. It utilizes the AWS global network to direct traffic along the shortest path with minimal packet loss and latency. Global Accelerator enhances the availability and performance of applications by intelligently routing traffic to the nearest AWS Edge Location.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f01f0f7b-5bc4-4c06-a7f1-a14e3f3f47de)

![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/1f68b8b6-25bf-4ec3-a277-01cb212f016c)

DNS Name
Global Accelerator assigns each accelerator a default DNS name such as a1234567890abcdef.awsglobalaccelerator.com that points to static IP address.These IP Addresses are anycast (Anycast IP — multiple servers holds same IP and helps to route request to nearest server.) from the AWS edge network.
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/2839dacf-ac31-492d-87fe-6acb0162b732)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/8fa58743-89f8-4363-aeaa-2291b6f30325)

# AWS Security Hub check findings of different integrations (2024/06/30)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f80a625b-28f2-45c2-9352-a1c43fc0ad5f)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/f478ce98-a0be-4f51-9bb4-44530396d5b4)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/922e0633-706d-48b2-856d-f80bf8ce1cd5)

# Vulnerability scan  (2024/06/30)
Vulnerability scanning is a key control within frameworks like SOC 2, ISO 27001, NIST 800-53.a vulnerability scanner is just an application that automatically tries to collect information about the devices it interacts with. 
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/087223b0-7c17-4e91-8922-2caead3ed406)
![image](https://github.com/xiongye77/aws_sysops_tasks/assets/36766101/dc37a567-ab6c-4f92-b825-5082c912e084)



# AWS Direct Connect Gateway (2024/08/05)
![image](https://github.com/user-attachments/assets/3febe474-bd92-44bc-8e5d-fd2abbf851ed)


# AWS Todo list app  (2024/08/11)
![image](https://github.com/user-attachments/assets/3ac25af3-fa13-400f-823e-2e5b6cc295d2)


# AWS Event Driven Architecture (2024/08/14)
An event-driven architecture uses events to trigger and communicate between decoupled services and is common in modern applications built with microservices. An event is a change in state, or an update, like an item being placed in a shopping cart on an e-commerce website.
![image](https://github.com/user-attachments/assets/e1c30729-787f-4ea7-87ef-0bb29038ce40)
![image](https://github.com/user-attachments/assets/95084cd5-d5bb-484e-a869-613ed5c0ad4e)
![image](https://github.com/user-attachments/assets/50b9aef2-5699-422a-8e2d-c1fde1705486)
![image](https://github.com/user-attachments/assets/cabaf897-4bfc-4600-ba3d-85d37c61f842)
![image](https://github.com/user-attachments/assets/97144518-53e0-4f7e-ab9d-d4620f220f01)
![image](https://github.com/user-attachments/assets/aae0bf80-c3fc-4b4c-a56e-54c5028f8e5a)

# AWS Event Bridge Pipes
![image](https://github.com/user-attachments/assets/6d08140b-79b4-4cb0-9be8-33863574defe)

![image](https://github.com/user-attachments/assets/329f0051-ab35-439f-a921-222e18d9f2d4)

# AWS Dynamodb could not use sql join and aggregate between tables 
![image](https://github.com/user-attachments/assets/9233cbb3-fa63-470d-9638-321ac14bb563)
![image](https://github.com/user-attachments/assets/2afb0aa5-e424-4e08-bf82-2620e3c96b9c)

# AWS Application Composer and CodeWhisperer 
![image](https://github.com/user-attachments/assets/ec09f3d7-d114-4192-9b7c-7dc05379c28b)


# Amazon Kinesis Data Firehose (2024/08/24)
The main purpose of Amazon Kinesis Data Firehose is similar to KDS – that is, to provide a platform for streaming data. However, the key differentiation is that Firehose provides a white-glove service when it comes to specific destinations. What this means is that for certain destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and some other HTTP endpoints, Firehose will do all the heavy lifting to ensure that the data, when delivered to these target destinations, is directly ready for consumption by the users.
![image](https://github.com/user-attachments/assets/899f7c28-0ebe-4bf9-8882-0e417c0581f6)



# AWS DMS 
instead of S3 as the target for DMS, we make KDS the target, which can then be chained with Kinesis Data Firehose. Finally, Firehose will put the final data files in S3. This way, you can leverage all the great features of Firehose to get an optimized data structure in the data lake
![image](https://github.com/user-attachments/assets/151b4c94-9ab7-44c7-941e-1fd59daefdc2)
![image](https://github.com/user-attachments/assets/cc941efe-37d2-40bd-9d2e-805e86a297a4)

![image](https://github.com/user-attachments/assets/41d5bb6c-dfe4-4ce5-8e84-80b847ad361c)
![image](https://github.com/user-attachments/assets/c9f8f3ba-fd04-4fd0-a653-a4c4bcd75fed)

![image](https://github.com/user-attachments/assets/5f621e0b-2d30-4fbd-aa13-7d5d57f6a9ad)
![image](https://github.com/user-attachments/assets/5f7b128c-9bdf-4571-9964-f09aca8f8a93)



# AWS API Gateway rest api vs http api (2024/08/26)
Key Differences:
REST API supports a broader range of direct integrations with AWS services using AWS service integrations.
HTTP API focuses on HTTP-based integrations, including support for AWS services via HTTP endpoints, and is optimized for simpler use cases with features like native JWT authorizers.
![image](https://github.com/user-attachments/assets/9277a65a-c227-4c86-9b57-c3d382fb885d)
![image](https://github.com/user-attachments/assets/9529f66e-1a3d-4230-88b7-6cca8b06508d)




# How Does Prometheus Work? 
![image](https://github.com/user-attachments/assets/d81c72d7-261a-4958-8027-060be6c2a00d)

https://github.com/xiongye77/aws_sysops_tasks/blob/main/Prometheus.txt
The Prometheus Server
Prometheus has a core component called the Prometheus server, which does the main monitoring work. This server is composed of three parts:

Time Series Database: This stores the collected metrics data (e.g., CPU usage, request latency) in a highly efficient format optimized for time-based queries.
Data Retriever (Scraper): This worker actively pulls metrics from various sources, including applications, databases, servers, and containers. It then sends the collected data to the time series database for storage.
HTTP Server API: This provides a way to query the stored metrics data. This API allows users to retrieve and visualize metrics through tools like the Prometheus dashboard, SigNoz, or Grafana.
![image](https://github.com/user-attachments/assets/8ed4ce50-e976-41a0-98a3-40db1cd11073)
![image](https://github.com/user-attachments/assets/8bf482c1-785f-4904-967b-286950dbedeb)

aws kafka  get-bootstrap-brokers --cluster-arn $CLUSTER_ARN | jq -r '.BootstrapBrokerString'

aws kafka describe-cluster --cluster-arn $CLUSTER_ARN --output json | jq ".ClusterInfo.ZookeeperConnectString"
export MYZK=$(aws kafka describe-cluster --cluster-arn $CLUSTER_ARN --output json | jq ".ClusterInfo.ZookeeperConnectString" | tr -d \")


./kafka-topics.sh --zookeeper $MYZK --list

By default, topics will be created with the default retention for the cluster (168 hours/7 days). 
If you want to change this (longer or shorter) you can override the retention value at the topic level.
./kafka-configs.sh --zookeeper $MYZK --alter --entity-name topic-name --entity-type topics  --add-config retention.ms=60000

This will set the retention to 512mb per partition:
./kafka-configs.sh --zookeeper $MYZK --alter --entity-name topic-name --entity-type topics --add-config retention.bytes=512000000



aws kafka list-clusters  | jq -r '.ClusterInfoList[].ClusterArn'

aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN

bin/kafka-consumer-groups.sh --bootstrap-server b-2.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9098,b-1.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9098  --command-config client.properties  --list



aws kafka describe-cluster   --cluster-arn arn:aws:kafka:us-east-1:582140066777:cluster/msk1/694ef560-fab8-4dfe-ab62-f7d099651fb5-17
aws kafka get-bootstrap-brokers  --cluster-arn arn:aws:kafka:us-east-1:582140066777:cluster/msk1/694ef560-fab8-4dfe-ab62-f7d099651fb5-17
aws kafka list-scram-secrets    --cluster-arn arn:aws:kafka:us-east-1:582140066777:cluster/msk1/694ef560-fab8-4dfe-ab62-f7d099651fb5-17
aws kafka list-nodes  --cluster-arn  arn:aws:kafka:us-east-1:582140066777:cluster/msk1/694ef560-fab8-4dfe-ab62-f7d099651fb5-17
bin/kafka-topics.sh  --bootstrap-server b-2.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096,b-1.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096   --create  --topic my-topic  --partitions 3   --replication-factor 2  --command-config client.properties.sasl_ssl
bin/kafka-topics.sh  --bootstrap-server b-2.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096,b-1.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096   --command-config client.properties.sasl_ssl  --alter  --topic my-topic   --partitions 6
bin/kafka-topics.sh  --bootstrap-server  b-2.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096,b-1.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096   --describe  --topic my-topic --command-config client.properties.sasl_ssl
bin/kafka-consumer-groups.sh  --bootstrap-server  b-2.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096,b-1.msk1.0g6eig.c17.kafka.us-east-1.amazonaws.com:9096   --command-config client.properties.sasl_ssl  --list

aws kafka list-nodes \
  --cluster-arn <your-cluster-arn> \
  --query 'NodeInfoList[*].[NodeId,BrokerNodeInfo.ClientBroker]' \
  --output text

  
bin/kafka-log-dirs.sh --bootstrap-server $brokers --describe | sed -n '/^{/,/}$/p' | jq '[.brokers[].logDirs[].partitions[] | select(.partition | startswith("topic-name")) | {partition: .partition, size: .size}]'

bin/kafka-log-dirs.sh --bootstrap-server "$brokers" --describe | \
  sed -n '/^{/,/}$/p' | \
  jq '[.brokers[] as $b | $b.logDirs[].partitions[] 
       | select(.partition | startswith("producer-demo")) 
       | {broker: $b.broker, partition: .partition, size: .size}]'

bin/kafka-log-dirs.sh --bootstrap-server "$brokers" --describe | \
  sed -n '/^{/,/}$/p' | \
  jq '[.brokers[] as $b | $b.logDirs[] as $ld | $ld.partitions[] 
       | select(.partition | startswith("topic-name")) 
       | {
           broker: $b.broker, 
           logDir: $ld.logDir, 
           partition: .partition, 
           size: .size
         }]'

  
Partition producer-demo-0 currently consumes ~5 MB (5,242,880 bytes) of disk space for its log segments on the broker.










When you add brokers to your Amazon MSK cluster, Kafka doesn't automatically redistribute the existing partitions to the new brokers. This means your new brokers remain idle until you explicitly reassign partitions to them. Here's what happens during partition reassignment:

What Partition Reassignment Does
Topic Selection

You identify which topics need redistribution
You can choose specific topics or redistribute all topics
For large clusters, selective redistribution helps manage the impact
Reassignment Planning

The kafka-reassign-partitions tool analyzes your current distribution
It generates an optimal layout across all available brokers
You can review and customize the proposed plan
Execution

Kafka begins moving partition data to new brokers
Replication ensures data consistency during transfer
Leader elections occur for redistributed partitions
Monitoring

Track progress of partition movements
Verify even distribution across all brokers
Monitor cluster performance metrics
This guide walks you through each step to ensure a successful partition redistribution across your expanded MSK cluster.

Step 1: Prepare for Partition Reassignment
First, examine your current partition distribution and create a reassignment plan.

View your current partition allocation:
cd /home/ec2-user/kafka
bin/kafka-topics.sh --bootstrap-server $brokers --describe --topic producer-demo

Example output: Current partition allocation

Note: The leader brokers are currently limited to IDs 1, 2, and 3.

Check the size of the topics-to-move
bin/kafka-log-dirs.sh --bootstrap-server $brokers --describe | sed -n '/^{/,/}$/p' | jq '[.brokers[].logDirs[].partitions[] | select(.partition | startswith("producer-demo")) | {partition: .partition, size: .size}]'

Example output: Current partition allocation

Create a topic migration file:
Create a file named topics-to-move.json with the following content:

cat <<EOF > topics-to-move.json
{ "topics": [ { "topic" : "producer-demo"}], "version":1}
EOF

Generate a reassignment plan:
bin/kafka-reassign-partitions.sh \
  --bootstrap-server $brokers \
  --topics-to-move-json-file topics-to-move.json \
  --broker-list "1,2,3,4,5,6" \
  --generate | \
  awk -F: '/Proposed partition reassignment configuration/ { getline; print $0 }' | \
  jq . > expand-cluster-reassignment.json

This command:

Creates a proposed partition layout
Includes all brokers (1-6) in the distribution
Saves the plan to expand-cluster-reassignment.json
Important: Save the current partition assignment displayed in the output. You can use this for rollback if needed.

Step 2: Execute the Reassignment
IMPORTANT!
Before proceeding, note down the time of the start of the reassignment
Apply the new partition configuration:
bin/kafka-reassign-partitions.sh \
  --bootstrap-server $brokers \
  --reassignment-json-file expand-cluster-reassignment.json \
  --execute

Monitor the reassignment progress:
bin/kafka-reassign-partitions.sh \
  --bootstrap-server $brokers \
  --reassignment-json-file expand-cluster-reassignment.json \
  --verify

Verify the new partition distribution:
bin/kafka-topics.sh --bootstrap-server $brokers --describe --topic producer-demo

Example output: New partition allocation

Note: The leader brokers now span all six brokers, indicating successful redistribution.

Step 3: Monitor Cluster Performance
Open the CloudWatch dashboard
Select the following metrics:
Topic: producer-demo
Metric Name: BytesInPerSec
Time range: 1 hour
Note when you started the partition reassignment and how long it took that the new brokers are taking traffic.
Example dashboard: Cluster performance metrics

To create a graph for the total troughput, click on Add math then select Common and choose Sum
Choose the Sum function

Observe that the cluster supported around ~37MBps and after the partition reassignment around ~58MBps
Choose the Sum function

The metrics show:

Workload distributed across all 6 brokers
Average ingress rate ~10 MBps per broker
Performance within the recommended 15.6 MBps limit for express.m7g.large instances
Rolling Back Changes
If needed, you can revert to the original partition assignment:

bin/kafka-reassign-partitions.sh \
  --bootstrap-server $brokers \
  --reassignment-json-file original-state.json \
  --execute

Note: This rolls back partition assignments only, not cluster size changes.


Kafka Terms
Broker - the individual kafka binary running on a host, or the server running kafka. This is the main Kafka server/service.

Cluster - a collection of brokers that are coordinating and working together to service producers and consumers

Controller - a Kafka service process that keeps track of and controls partition assignment, broker health and status, publishes cluster health metrics, etc. The controller is elected from the available brokers.

Consumer - a program that reads messages from kafka.

Consumer Group - a collection of consumers that all work together to consume messages from Kafka, coordinating their work and recovering/rebalancing if the group size changes.

Consumer Lag - when a consumer is reading messages from a partition, the difference between where the offset the consumer is reading and the offset where the producer is writing is called Lag. Too much lag means that consumers aren't able to keep up with the incoming data and latency is being added to your processing.

ISR - An In-Sync Replica of a partition. To be In-Sync a message must stay within a fixed number of offsets from the Leader. If it falls behind its no longer an ISR and cannot be made Leader until it comes back in to sync.

Leader - one of the replicas of a partition which is elected (or assigned) the role of handling ingest for that partition. All writes happen to the leader, and data is replicated from the leader to replicas.

Leader election - Leaders are elected from brokers that have an In-Sync Replica (ISR) of the data

Message - a constrained bit of data - could be a JSON object, a log line, an image file, a database transaction

Offline Partition - a partition that is no longer available to be produced to or consumed from because no brokers have a copy of the partition and so cannot make it available. This should never happen in a cluster, and is an indication that something has gone wrong.

Offset - a constantly increasing number that is a unique identifier for a message.

Partition - a portion of a Topic. Topics are divided up into partitions as a method of scaling throughput, as well as allowing for strict message ordering with appropriate configuration.

Producer - a program that writes messages to Kafka.

Topic - a collection of messages that are generally related. Messages are produced to a topic, and consumed from a topic. Topics can be consumed by multiple consumers.

Replica - a copy of a partition held on another broker in the cluster. Automatically kept in sync with the leader.

Replication lag - replicas of a partition will replicate data from the leader, reading Offsets in order. The difference between the Replicas offset and the Leaders latest offset is Replication Lag. High replication lag will cause a replica to no longer be an In-Sync Replica, and usually indicates that a cluster or partition is overloaded.

Unclean Leader Election - When there is a leade election, but there are no In-Sync Replicas (ISRs) available. And unclean leader election means that data was lost.

Zookeeper - a distributed data storage engine that Kafka uses to store metadata about the service, as well as using the Zookeeper leader election protocol to makde decisions about which broker is the leader for which partitions.




Monitoring consumer lag allows you to identify slow or stuck consumers that aren't keeping up with the latest data available in a topic. When necessary, you can then take remedial actions, such as scaling or rebooting those consumers. To monitor consumer lag, you can use Amazon CloudWatch or open monitoring with Prometheus.

Consumer lag metrics quantify the difference between the latest data written to your topics and the data read by your applications. Amazon MSK provides the following consumer-lag metrics, which you can get through Amazon CloudWatch or through open monitoring with Prometheus: EstimatedMaxTimeLag, EstimatedTimeLag, MaxOffsetLag, OffsetLag, and SumOffsetLag.


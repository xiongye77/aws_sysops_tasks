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

  
bin/kafka-log-dirs.sh --bootstrap-server $brokers --describe | sed -n '/^{/,/}$/p' | jq '[.brokers[].logDirs[].partitions[] | select(.partition | startswith("producer-demo")) | {partition: .partition, size: .size}]'

bin/kafka-log-dirs.sh --bootstrap-server "$brokers" --describe | \
  sed -n '/^{/,/}$/p' | \
  jq '[.brokers[] as $b | $b.logDirs[].partitions[] 
       | select(.partition | startswith("producer-demo")) 
       | {broker: $b.broker, partition: .partition, size: .size}]'

bin/kafka-log-dirs.sh --bootstrap-server "$brokers" --describe | \
  sed -n '/^{/,/}$/p' | \
  jq '[.brokers[] as $b | $b.logDirs[] as $ld | $ld.partitions[] 
       | select(.partition | startswith("producer-demo")) 
       | {
           broker: $b.broker, 
           logDir: $ld.logDir, 
           partition: .partition, 
           size: .size
         }]'

  
Partition producer-demo-0 currently consumes ~5 MB (5,242,880 bytes) of disk space for its log segments on the broker.

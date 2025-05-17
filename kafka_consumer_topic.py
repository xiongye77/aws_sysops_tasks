# The error KafkaError._PARTITION_EOF in Kafka (typically encountered when using the confluent-kafka-python client) is not an actual error, 
# but rather a signal that the consumer has reached the end of a partition — meaning there is currently no more data to consume from that partition.
# You can safely ignore or log this and continue polling.
# Wait up to 1.0 seconds for a new message from the Kafka topic. If no message arrives within that time, return None.
# Kafka consumers pull messages, not push. So: You continuously call poll() to retrieve new messages.
# The timeout prevents the loop from blocking forever.

# if your Kafka producers serialize messages using Protobuf, then you must deserialize them using the same Protobuf schema on the consumer side.
# Kafka itself is just a transport. It stores and delivers bytes. If your messages are serialized using Protobuf (rather than plain JSON or string), then on the consumer side:
# The message will arrive as a binary blob (msg.value() in Python)
# You need to decode it using the matching .proto schema
# Use the Protobuf class generated from the .proto file to deserialize



# Apache Kafka is a distributed event streaming platform designed for high-throughput, fault-tolerant, and real-time data ingestion and processing. 
It solves problems related to:
Decoupling data producers and consumers
Persisting real-time streams durably
Handling high-scale message processing with replay support


#What are the main components of Kafka?

Producer: Sends messages to Kafka topics.
Consumer: Subscribes to topics and reads messages.
Topic: Logical channel to organize messages.
Partition: Subdivision of a topic; enables parallelism.
Broker: Kafka server that stores data and serves clients.
Zookeeper (pre-Kafka 3.x): Coordinates cluster metadata (now replaced by KRaft).

#How do you handle schema evolution in Kafka?

Use a schema registry (like Confluent or AWS Glue). It enforces schema compatibility (backward, forward, full). Producers/consumers validate messages based on schema versions.


# If your multiple Kubernetes pods are running Kafka consumers and are all configured with the same group.id, then they collectively form a Kafka consumer group, 
allowing you to scale consumption horizontally and process Kafka messages in parallel.   
Kafka assigns topic partitions across those pods automatically.Each pod gets a subset of partitions, so messages are processed in parallel.

    
from confluent_kafka import Consumer
import json, re, uuid, sys
import traceback

# ---------- 1.  Configuration -------------------------------------------------
BOOTSTRAP      = "pkc-xxxxx.us-west-2.aws.confluent.cloud:9092"
API_KEY        = "XXXXXXX"
API_SECRET     = "YYYYYYY"
TOPIC          = "stage.xxxx.behavioural-event.xxxx-appplat-usageanalytics.all-behavioural.v1"

conf = {
    "bootstrap.servers":  BOOTSTRAP,
    "security.protocol":  "SASL_SSL",
    "sasl.mechanisms":    "PLAIN",
    "sasl.username":      API_KEY,
    "sasl.password":      API_SECRET,
    "enable.auto.offset.store": False,
    "group.id":           "stage.sPMDcdp3hC7TnaDmPiBtjf-cdp-subscriber-group",
    "auto.offset.reset":  "earliest",
}


# ---------- 3.  Create consumer & subscribe ----------------------------------
consumer = Consumer(conf)
consumer.subscribe([TOPIC])

# Wait for partition assignment (optional, but nice for debugging)
print("Waiting for partition assignment …", file=sys.stderr)
while not consumer.assignment():
    consumer.poll(0.1)
print("Assigned partitions:", consumer.assignment(), file=sys.stderr)


# ---------- 4.  Consume loop --------------------------------------------------

EMPTY_POLLS_ALLOWED = 3000        # stop after 30 × 1 s = 30 s idle
empty_polls = 0
seen = set()    
try:
    while empty_polls < EMPTY_POLLS_ALLOWED:
        msg = consumer.poll(1.0)
        # no record this second
        if msg is None:
            empty_polls += 1
            continue

        # reset idle counter
        #print("here")
        empty_polls = 0

        if msg.error():
           if msg.error().code() == KafkaError._PARTITION_EOF:
               continue
           else:
               self.logger.error(str(msg.error()))
               continue
        # decode safely
        try:
            decoded = msg.value().decode("utf-8", errors="ignore")  # Or use "ignore"
            #print(decoded)
            payload = decoded
            #print(payload) 
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            print("Error:", e)
            traceback.print_exc()  # Print full traceback
            continue

        m = re.search(r'\b(\w*EventV[1-5])\b', payload)
        if not m:
            continue

        event_name = m.group(1)

        # ------------ print only if never seen before -------------
        if event_name not in seen:
            seen.add(event_name)
            print(f"New event type ➡️  {event_name}")
finally:
    consumer.close()

print("\nDistinct event names in this run:")
for name in sorted(seen):
    print(" •", name)

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

#producer.py

from kafka import KafkaProducer
from confluent_kafka import Producer
from aws_schema_registry.adapter.kafka import KafkaSerializer
from common import schema_registry_client, avro_schema, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, User, SCHEMA_NAME
import socket
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token('us-east-1')
        return token
tp = MSKTokenProvider()


def create_producer():
    serializer = KafkaSerializer(schema_registry_client)
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=serializer,
        key_serializer=str.encode,
        security_protocol='SASL_SSL',  # Add this line
        sasl_mechanism='OAUTHBEARER',
        sasl_oauth_token_provider=tp,
        client_id=socket.gethostname(),
    )
    return producer

def send_message(producer, key, user_data):
    producer.send(KAFKA_TOPIC, key=str(key), value=(user_data, avro_schema))
    producer.flush()
    print(f"Produced message with key: {key}, data: {user_data}")

if __name__ == "__main__":
    producer = create_producer()
    try:
        user1 = User(id=1, name="Alice", email="alice@example.com", properties={"country": "USA"})
        send_message(producer, user1.id, user1.to_dict())

        user2 = User(id=2, name="Bob", email="bob@example.com", properties={"city": "London"})
        send_message(producer, user2.id, user2.to_dict())
    finally:
        producer.close()



consumer.py
from kafka import KafkaConsumer
from aws_schema_registry.adapter.kafka import KafkaDeserializer
from common import schema_registry_client, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
import socket
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token('us-east-1')
        return token
tp = MSKTokenProvider()

def create_consumer():
    deserializer = KafkaDeserializer(schema_registry_client)
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="my-consumer-group",
        value_deserializer=deserializer,
        key_deserializer=bytes.decode,
        auto_offset_reset="earliest",
        security_protocol='SASL_SSL',  # Add this line
        sasl_mechanism='OAUTHBEARER',
        sasl_oauth_token_provider=tp,
        client_id=socket.gethostname(),
    )
    consumer.subscribe([KAFKA_TOPIC])
    return consumer

def consume_messages(consumer):
    print("Consuming messages...")
    for message in consumer:
        if message.value is not None:
            print(f"Received message: Key = {message.key}, Value = {message.value}")
        else:
            print(f"Received message with empty value: Key = {message.key}")

if __name__ == "__main__":
    consumer = create_consumer()
    try:
        consume_messages(consumer)
    except KeyboardInterrupt:
        print("Consumer stopped by user.")
    finally:
        consumer.close()



common.py
import boto3
from aws_schema_registry.client import SchemaRegistryClient  # Changed import
from aws_schema_registry.avro import AvroSchema # Changed import
from dataclasses import dataclass, field
from typing import Dict

# --- Configuration ---
REGION_NAME = "us-east-1"
GLUE_REGISTRY_NAME = "glue-schema-registry-kafka-topic"
KAFKA_BOOTSTRAP_SERVERS = ["b-1.msk1.twjhm8.c17.kafka.us-east-1.amazonaws.com:9098","b-2.msk1.twjhm8.c17.kafka.us-east-1.amazonaws.com:9098"]
KAFKA_TOPIC = "my-topic"
SCHEMA_NAME = "topic1-schema"

# --- Define Data Class ---
@dataclass
class User:
    id: int = field()
    name: str = field()
    email: str = field()
    properties: Dict[str, str] = field(default_factory=dict)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "properties": self.properties
        }

# --- Initialize AWS Glue Schema Registry Client ---
glue_client = boto3.client("glue", region_name=REGION_NAME)
schema_registry_client = SchemaRegistryClient(glue_client, registry_name=GLUE_REGISTRY_NAME) # Changed Class Name
print(schema_registry_client)
# --- Define Avro Schema ---
avro_schema_str = """
{
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "properties", "type": {"type": "map", "values": "string"}}
    ]
}
"""
avro_schema = AvroSchema(avro_schema_str) # Changed Class Name

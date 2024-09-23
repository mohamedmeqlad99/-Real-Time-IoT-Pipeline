from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'iot_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='iot_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received message: {message.value}")  # Process the message

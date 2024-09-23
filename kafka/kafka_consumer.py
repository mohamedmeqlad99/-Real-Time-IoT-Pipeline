from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'iot_data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_data():
    for message in consumer:
        print(f"Consumed message: {message.value}")

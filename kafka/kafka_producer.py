from kafka import KafkaProducer
import json
from scripts.data_generate import generate_iot_data

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def produce_data():
    while True:
        data = generate_iot_data()
        producer.send('iot_data', value=data)

from faker import Faker
import random
import time
from kafka import KafkaProducer
import json

fake = Faker()

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_iot_data():
    while True:
        data = {
            'device_id': fake.uuid4(),
            'temperature': round(random.uniform(20.0, 40.0), 2),
            'humidity': round(random.uniform(30.0, 70.0), 2),
            'timestamp': fake.date_time_this_year().isoformat()
        }
        print(f"Sending: {data}")
        producer.send('iot_topic', value=data)
        time.sleep(1)  

generate_iot_data()

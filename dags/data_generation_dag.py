from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker
import json
import random
import time

fake = Faker()

def generate_fake_data():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    for _ in range(100): 
        data = {
            'device_id': random.randint(1, 100),  
            'temperature': random.randint(20, 30),
            'humidity': random.randint(30, 70),
            'timestamp': fake.date_time_this_month().isoformat()
        }
        producer.send('iot_data', json.dumps(data).encode('utf-8'))
        print(f"Sent data: {data}")
        time.sleep(1)  

with DAG(
    dag_id='data_generation_dag',
    schedule_interval='@once',  
    start_date=datetime.now(),
    catchup=False
) as dag:
    generate_data_task = PythonOperator(
        task_id='generate_fake_data',
        python_callable=generate_fake_data
    )

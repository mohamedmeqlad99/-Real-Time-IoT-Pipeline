# dags/data_producer_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
}

dag = DAG('data_producer', default_args=default_args, schedule_interval='@daily')

def run_kafka_producer():
    subprocess.Popen(['python', '/path/to/kafka/kafka_producer.py'])

data_generator_task = PythonOperator(
    task_id='run_kafka_producer',
    python_callable=run_kafka_producer,
    dag=dag,
)

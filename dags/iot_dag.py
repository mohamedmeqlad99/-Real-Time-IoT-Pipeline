from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import subprocess

#declare the args 
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'iot_data_generation_dag',
    default_args=default_args,
    description='A simple DAG to generate IoT data',
    schedule=timedelta(minutes=5),
)

def generate_iot_data():
    script_path = '/home/meqlad/-Real-Time-IoT-Pipeline/scripts/data_generate.py'
    subprocess.run(['python',script_path])

run_iot_data_task = PythonOperator(
    task_id='run_iot_data_script',
    python_callable=generate_iot_data,
    dag=dag,
)

    

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.apache.kafka.hooks.kafka import KafkaConsumer
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(dag_id='iot_data_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    
    start = DummyOperator(task_id='start')

    spark_task = SparkSubmitOperator(
        task_id='spark_process_iot_data',
        application='/path/to/spark/process_iot_data.py',
        conn_id='spark_default',
        verbose=True
    )

    start >> spark_task

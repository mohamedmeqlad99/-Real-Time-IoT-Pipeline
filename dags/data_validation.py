from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import logging
import psycopg2
from scripts.validation import validate_iot_data

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'iot_data_validation_dag',
    default_args=default_args,
    description='Validate IoT data before storing in PostgreSQL',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    def validate_data(data):

            data = json.loads(data)
            device_id = data.get('device_id')
            timestamp = data.get('timestamp')
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            battery_level = data.get('battery_level')
            device_status = data.get('device_status')

            # Check for missing fields
            if not all([device_id, timestamp, temperature, humidity, battery_level, device_status]):
                logging.error(f"Missing fields in data: {data}")
                return None

            # Validate ranges
        

    def store_valid_data_to_postgres(valid_data):
        if valid_data is None:
            logging.info("No valid data to store")
            return

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_username",
            password="your_password",
            host="your_db_host",
            port="5432"
        )
        cursor = conn.cursor()

        # Insert valid data into PostgreSQL
        insert_query = """
        INSERT INTO iot_data (device_id, timestamp, temperature, humidity, battery_level, device_status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            valid_data['device_id'], valid_data['timestamp'], valid_data['temperature'],
            valid_data['humidity'], valid_data['battery_level'], valid_data['device_status']
        ))
        conn.commit()
        cursor.close()
        conn.close()

    def validate_and_store_data():
        # Read data from Kafka (assuming KafkaConsumer is already set up)
        consumer = KafkaConsumer('iot_data_topic', bootstrap_servers='localhost:9092')
        
        for message in consumer:
            iot_data = message.value.decode('utf-8')
            valid_data = validate_data(iot_data)
            store_valid_data_to_postgres(valid_data)

    # Define tasks
    validate_and_store_task = PythonOperator(
        task_id='validate_and_store_data',
        python_callable=validate_and_store_data,
    )

    validate_and_store_task

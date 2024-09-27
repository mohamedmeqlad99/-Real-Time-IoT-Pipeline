from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2

def backup_to_postgres():
    conn = psycopg2.connect(
        dbname="iot_db",
        user="meqlad",
        password="meqlad",
        host="postgres"
    )
    cur = conn.cursor()
    
    # Assuming data is saved as CSV
    with open('/path/to/processed_data.csv', 'r') as f:
        next(f)  # Skip header
        cur.copy_from(f, 'iot_backup', sep=',')
    
    conn.commit()
    cur.close()
    conn.close()

default_args = {
    'start_date': datetime.now(),
}

with DAG('backup_to_postgres', default_args=default_args, schedule_interval='@daily') as dag:
    backup_task = PythonOperator(
        task_id='backup_to_postgres_task',
        python_callable=backup_to_postgres
    )

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import psycopg2
import csv

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

dag = DAG(
    'data_backup_dag',
    default_args=default_args,
    description='DAG to back up data from PostgreSQL to CSV',
    schedule_interval='@daily',
)

def backup_data_to_csv():
    conn = psycopg2.connect(dbname="iot_db", user="iot_user", password="iot_pass", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM iot_data")
    
    with open('/usr/local/airflow/data/iot_data_backup.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    
    cursor.close()
    conn.close()

backup_task = PythonOperator(
    task_id='backup_data_to_csv',
    python_callable=backup_data_to_csv,
    dag=dag,
)

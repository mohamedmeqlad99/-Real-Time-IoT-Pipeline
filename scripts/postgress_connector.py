import psycopg2
import json

def connect_to_postgres():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="your_db_host",
        port="5432"
    )
    return conn

def backup_iot_data_to_postgres():
    with open('iot_data.json', 'r') as file:
        data_list = json.load(file)

    conn = connect_to_postgres()
    cursor = conn.cursor()

    for data in data_list:
        query = """
        INSERT INTO iot_data_backup (device_id, timestamp, temperature, humidity, battery_level, device_status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['device_id'], data['timestamp'], data['temperature'], data['humidity'], data['battery_level'], data['device_status']))

    conn.commit()
    cursor.close()
    conn.close()

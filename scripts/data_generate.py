from faker import Faker
import time
import json
import random
import os
import logging

# Setup logging
logging.basicConfig(filename='iot_data.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

fake = Faker()

device_list = [fake.uuid4() for _ in range(100)]

def generate_iot_data(device_id):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    battery_level = random.randint(10, 100)
    device_status = random.choice(["active", "inactive", "faulty"])

    return {
        'device_id': device_id,
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity,
        'battery_level': battery_level,
        'device_status': device_status
    }

json_file = 'iot_data.json'

def load_existing_data():
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
    logging.info(f"Data written to {json_file}")

existing_data = load_existing_data()

while True:
    random.shuffle(device_list)
    batch_data = []

    logging.info("Generating data...")
    for device_id in device_list:
        data = generate_iot_data(device_id)
        batch_data.append(data)
        time.sleep(1)

    logging.info("Appending batch data to JSON...")
    existing_data.extend(batch_data)
    save_data(existing_data)
    logging.info("Batch data appended successfully.")

from faker import Faker
import time
import json
import random
import os

fake = Faker()

# Generate a list of 100 unique devices
device_list = [fake.uuid4() for _ in range(100)]

def generate_iot_data(device_id):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(15.0, 35.0), 2)  # Temperature in °C
    humidity = round(random.uniform(30.0, 90.0), 2)  # Humidity percentage
    battery_level = random.randint(10, 100)  # Battery percentage
    device_status = random.choice(["active", "inactive", "faulty"])  # Random status

    return {
        'device_id': device_id,
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity,
        'battery_level': battery_level,
        'device_status': device_status
    }

# Create a directory for JSON files if it does not exist
os.makedirs('json_data', exist_ok=True)

def write_data_to_json(data, file_index):
    filename = f'json_data/iteration_{file_index}.json'
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

file_index = 1

while True:
    random.shuffle(device_list)  # Shuffle the device list before each cycle
    batch_data = []

    for device_id in device_list:  # Iterate through all 100 devices
        data = generate_iot_data(device_id)
        batch_data.append(data)
        time.sleep(1)  # Wait for 1 second before generating the next record
    
    write_data_to_json(batch_data, file_index)
    file_index += 1

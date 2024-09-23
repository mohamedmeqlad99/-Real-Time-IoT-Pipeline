from faker import Faker
import time
import json
import random

fake = Faker()

def generate_iot_data():
    device_id = fake.uuid4()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    battery_level = random.randint(10, 100)
    device_status = random.choice(["active", "inactive", "faulty"])

    iot_data = {
        'device_id': device_id,
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity,
        'battery_level': battery_level,
        'device_status': device_status
    }
    return json.dumps(iot_data)

while True:
    data = generate_iot_data()
    # Send data to Kafka
    print(data)  # Replace with Kafka producer logic
    time.sleep(1)
from faker import Faker
import time
import json
import random

fake = Faker()

def generate_iot_data():
    device_id = fake.uuid4()  # Random device ID
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(15.0, 35.0), 2)  # Temperature in °C
    humidity = round(random.uniform(30.0, 90.0), 2)  # Humidity percentage
    battery_level = random.randint(10, 100)  # Battery percentage
    device_status = random.choice(["active", "inactive", "faulty"])  # Random status
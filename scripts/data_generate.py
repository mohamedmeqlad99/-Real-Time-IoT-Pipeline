from faker import Faker
import time
import csv
import random

fake = Faker()

# Generate a list of 100 unique devices
device_list = [fake.uuid4() for _ in range(100)]

def generate_iot_data(device_id):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(15.0, 35.0), 2)  # Temperature in °C
    humidity = round(random.uniform(30.0, 90.0), 2)  # Humidity percentage
    battery_level = random.randint(10, 100)  # Battery percentage
    device_status = random.choice(["active", "inactive", "faulty"])  # Random status

    return [device_id, timestamp, temperature, humidity, battery_level, device_status]

# Write data to CSV file
with open('iot_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["device_id", "timestamp", "temperature", "humidity", "battery_level", "device_status"])
    
    while True:
        random.shuffle(device_list) 
        
        for device_id in device_list:  
            data = generate_iot_data(device_id)
            writer.writerow(data)
            time.sleep(1) 


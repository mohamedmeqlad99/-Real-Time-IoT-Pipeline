import json
def validate_iot_data():
    with open('iot_data.json', 'r') as file:
        data_list = json.load(file)

    for data in data_list:
        if not (15.0 <= data['temperature'] <= 35.0):
            print(f"Invalid temperature: {data['temperature']}")
        if not (30.0 <= data['humidity'] <= 90.0):
            print(f"Invalid humidity: {data['humidity']}")
        if not (10 <= data['battery_level'] <= 100):
            print(f"Invalid battery level: {data['battery_level']}")
        if data['device_status'] not in ["active", "inactive", "faulty"]:
            print(f"Invalid device status: {data['device_status']}")

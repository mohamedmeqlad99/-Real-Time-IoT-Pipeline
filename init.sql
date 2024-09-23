CREATE DATABASE iot_db;
CREATE USER iot_user WITH PASSWORD 'iot_pass';
GRANT ALL PRIVILEGES ON DATABASE iot_db TO iot_user;

\connect iot_db

CREATE TABLE iot_data (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(255),
    timestamp TIMESTAMP,
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    battery_level INT,
    device_status VARCHAR(50)
);
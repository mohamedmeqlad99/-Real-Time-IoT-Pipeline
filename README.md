# **IoT Data Engineering Pipeline**


![Screenshot from 2024-09-27 16-10-27](https://github.com/user-attachments/assets/d990c778-a8cc-4e45-822c-ad885ab9c3f5)


This project demonstrates a complete IoT data engineering pipeline. The pipeline simulates IoT data using Faker, processes it in real-time using Kafka and Spark, backs up the processed data to PostgreSQL, and visualizes the data using Matplotlib.

---

## **Key Components**

### 1. **Data Generation (Faker & Kafka Producer)**

- Uses the **Faker** Python package to simulate IoT data (e.g., temperature, humidity, timestamps).
- This data is streamed in real-time to a **Kafka** topic (`iot_topic`).
  
File: `kafka/producer.py`

### 2. **Data Ingestion (Kafka Broker)**

- Kafka manages the streaming data between the **Kafka Producer** and downstream components like **Spark**.
- Kafka is configured in **Docker Compose** for easy setup.

### 3. **Data Processing (Spark)**

- **Apache Spark** consumes data from Kafka, processes it (e.g., filters out unwanted records), and saves the processed data to a file or passes it on.
  
File: `spark/process_iot_data.py`

### 4. **Orchestration (Apache Airflow)**

- **Airflow** is used to manage the end-to-end pipeline:
  - **DAG 1**: `iot_data_pipeline.py` for triggering the data generation and processing.
  - **DAG 2**: `backup_to_postgres.py` for automating data backups to PostgreSQL.
  
Files: `dags/iot_data_pipeline.py`, `dags/backup_to_postgres.py`

### 5. **Data Backup (PostgreSQL)**

- Processed data is backed up to **PostgreSQL** for long-term storage and querying.
- PostgreSQL is set up using Docker and is accessible at `localhost:5432`.

### 6. **Data Visualization (Matplotlib)**

- Visualizes trends in IoT data, such as temperature variations over time, using **Matplotlib**.

File: `visualizations/visualize_data.py`

---

## **Technologies Used**

- **Kafka**: For data ingestion and real-time streaming.
- **Faker**: For simulating IoT data.
- **Spark**: For distributed data processing.
- **PostgreSQL**: For data backup and storage.
- **Airflow**: For pipeline orchestration.
- **Matplotlib**: For data visualization.
- **Docker**: To containerize and orchestrate all services.

---

## **How to Run the Project**

### **1. Prerequisites**

- **Docker** and **Docker Compose** should be installed on your system.

### **2. Setup and Run the Pipeline**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/iot_data_pipeline.git
    cd iot_data_pipeline
    ```

2. **Build and start services**:

    ```bash
    docker-compose up --build
    ```

3. **Start Kafka Producer to generate IoT data**:

    ```bash
    python kafka/producer.py
    ```

4. **Access Airflow UI**:

    Airflow will be available at `http://localhost:8080`. You can manually trigger DAGs to start data processing and backups.

5. **Check PostgreSQL**:

    Connect 

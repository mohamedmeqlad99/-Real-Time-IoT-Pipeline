# Use the official Airflow image
FROM apache/airflow:2.6.0

# Install Python dependencies (Faker, etc.)
RUN pip install faker

# Copy the local files into the container
COPY ./iot_data_generator.py /opt/airflow/dags/iot_data_generator.py
COPY ./dags /opt/airflow/dags/

# Set the working directory
WORKDIR /opt/airflow

# Set up Airflow environment variables (you can adjust these)
ENV AIRFLOW_HOME=/opt/airflow

# Initialize Airflow DB and start services
CMD ["airflow", "scheduler"]

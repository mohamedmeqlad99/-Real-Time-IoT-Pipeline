from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IoTDataProcessing").getOrCreate()

df = spark.read.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "iot_topic").load()

# Transform the data (example: filter high temperatures)
processed_data = df.filter(df.temperature > 30)

# Save to CSV for backup
processed_data.write.csv("/path/to/processed_data.csv")

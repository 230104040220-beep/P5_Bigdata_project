from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("StreamingLayer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("transaction_id", IntegerType()),
    StructField("timestamp", StringType()),
    StructField("city", StringType()),
    StructField("product", StringType()),
    StructField("price", IntegerType())
])

df = spark.readStream \
    .schema(schema) \
    .json("stream_data")

df = df.withColumn("timestamp", to_timestamp("timestamp"))

query = df.writeStream \
    .format("parquet") \
    .option("path", "data/serving/stream") \
    .option("checkpointLocation", "logs/checkpoint") \
    .outputMode("append") \
    .start()

print("🔥 Streaming jalan...")

query.awaitTermination()
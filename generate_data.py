print("START GENERATE DATA...")
from pyspark.sql import SparkSession
import os

# =========================
# INIT SPARK
# =========================
spark = SparkSession.builder \
    .appName("GenerateDummyData") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# =========================
# BUAT DATA DUMMY
# =========================
data = [
    (1, "Laptop", "Electronics", 2, 15000000),
    (2, "Mouse", "Electronics", 5, 500000),
    (3, "Keyboard", "Electronics", 3, 750000),
    (4, "Sepatu", "Fashion", 2, 800000),
    (5, "Baju", "Fashion", 4, 600000),
    (6, "Tas", "Fashion", 1, 900000),
    (7, "Kopi", "Food", 10, 200000),
    (8, "Teh", "Food", 8, 150000),
    (9, "Snack", "Food", 15, 100000),
]

columns = ["customer_id", "product", "category", "quantity", "total_amount"]

df = spark.createDataFrame(data, columns)

# =========================
# SIMPAN KE PARQUET
# =========================
output_path = "data/clean/parquet"

if not os.path.exists("data/clean"):
    os.makedirs("data/clean")

df.write.mode("overwrite").parquet(output_path)

print("✅ Data parquet berhasil dibuat di:", output_path)

spark.stop()

print("SELESAI!")
from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import os

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("VisualizationLayer") \
    .master("local[*]") \
    .getOrCreate()

# Membaca data bersih
df = spark.read.parquet("data/clean/parquet/")

# Membuat folder reports jika belum ada
if not os.path.exists("reports"):
    os.makedirs("reports")

# Agregasi data untuk Grafik Revenue per Category
category_df = df.groupBy("category") \
    .sum("total_amount") \
    .toPandas()

# Mengurutkan data
category_df = category_df.sort_values("sum(total_amount)", ascending=False)

# Membuat Plot
plt.figure(figsize=(8,5))
plt.bar(category_df["category"], category_df["sum(total_amount)"])
plt.xticks(rotation=45)
plt.title("Revenue per Category")
plt.ylabel("Total Revenue")
plt.tight_layout()

# Menyimpan hasil visualisasi
plt.savefig("reports/category_revenue.png")
print("Visualization saved to reports/category_revenue.png")

spark.stop()

# E-Commerce Sales Analytics - Big Data Technology

Proyek ini adalah implementasi **Batch Analytics** menggunakan **Apache Spark** dan **Power BI** untuk menganalisis data transaksi e-commerce. Proyek ini bertujuan untuk memproses data mentah menjadi wawasan bisnis yang siap divisualisasikan.

## 🚀 Fitur Utama
* **Data Processing**: Membersihkan dan mentransformasi data mentah menggunakan PySpark.
* **Batch Analytics**: Menghitung total revenue, produk terlaris, dan pendapatan per kategori.
* **Data Visualization**: Dashboard interaktif menggunakan Power BI Desktop.

## 🛠️ Teknologi yang Digunakan
* **Python 3.12**
* **Apache Spark (PySpark)**
* **Power BI Desktop**
* **Visual Studio Code (WSL: Ubuntu)**

## 📂 Struktur Folder
* `scripts/`: Berisi file Python untuk pemrosesan data (`analytics_layer.py`).
* `data/serving/`: Output data hasil olah Spark dalam format CSV.
* `reports/`: Hasil ekspor grafik dalam format gambar.
* `bigdata_dashboard.pbix`: File project dashboard Power BI.

## 📊 Hasil Analisis
Dashboard yang dibuat mencakup tiga metrik utama:
1. **Total Revenue**: Menampilkan total pendapatan keseluruhan.
2. **Top Product**: Visualisasi produk dengan jumlah penjualan tertinggi.
3. **Revenue per Category**: Distribusi pendapatan berdasarkan kategori produk (Electronics, Fashion, Food).

## 📝 Cara Menjalankan
1. Jalankan script analytics:
   ```bash
   python scripts/analytics_layer.py

 * Pastikan muncul pesan ANALYTICS LAYER COMPLETED SUCCESS.
 * Buka file bigdata_dashboard.pbix di Power BI dan lakukan Refresh Data.
Dibuat oleh:
 * Nama: mahmudah
 * NIM: 230104040220

---

### Langkah Terakhir (Push ke GitHub):
Setelah file `README.md` disimpan, jalankan perintah cepat ini di terminal agar file muncul di halaman depan GitHub kamu:

1. `git add README.md`
2. `git commit -m "menambah dokumentasi readme"`
3. `git push origin main`

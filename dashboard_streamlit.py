import streamlit as st
import pandas as pd
import glob
import time

st.set_page_config(page_title="Real-Time Dashboard", layout="wide")

# --- Judul Dashboard ---
st.title("Real-Time E-Commerce Analytics Dashboard")

# --- Load Data ---
files = glob.glob("stream_data/*.json")

if files:
    df_list = [pd.read_json(f, lines=True) for f in files]
    df = pd.concat(df_list, ignore_index=True)
    # Pastikan kolom timestamp bertipe datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # --- 1. Key Metrics Section ---
    st.subheader("Key Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Transactions", len(df))
    m2.metric("Total Revenue", f"${df['price'].sum():,.0f}")
    m3.metric("Avg Transaction", f"${df['price'].mean():,.0f}")
    m4.metric("Cities", df['city'].nunique())

    st.divider()

    # --- 2. Bar Charts Section (Dua Kolom) ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by City")
        city_rev = df.groupby("city")["price"].sum()
        st.bar_chart(city_rev)

    with col2:
        st.subheader("Top Products")
        prod_rev = df.groupby("product")["price"].sum()
        st.bar_chart(prod_rev)

    # --- 3. Revenue Trend Section (Grafik Garis) ---
    st.subheader("Revenue Trend")
    # Mengelompokkan pendapatan berdasarkan waktu (menit)
    trend_data = df.set_index('timestamp').resample('1min')['price'].sum().fillna(0)
    st.line_chart(trend_data)

    # --- 4. Live Transactions Table ---
    st.subheader("Live Transactions")
    # Menampilkan 10 transaksi terakhir (terbaru di atas)
    st.dataframe(df.sort_values(by='timestamp', ascending=False).head(10), use_container_width=True)

else:
    st.info("Menunggu data masuk dari stream...")

# --- Auto Refresh ---
time.sleep(2)
st.rerun()
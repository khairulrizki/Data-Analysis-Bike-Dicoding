import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memasukkan data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Mapping untuk bulan
day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
hour_df['mnth'] = hour_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})

# Mapping untuk musim
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
hour_df['season'] = hour_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

# Mapping untuk kondisi cuaca
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})
hour_df['weathersit'] = hour_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Sidebar
st.sidebar.title("Filter Tanggal")
min_date_day = pd.to_datetime(day_df['dteday']).dt.date.min()
max_date_day = pd.to_datetime(day_df['dteday']).dt.date.max()
start_date_day, end_date_day = st.sidebar.date_input(
    "Rentang Waktu (Harian)",
    min_value=min_date_day,
    max_value=max_date_day,
    value=[min_date_day, max_date_day]
)

min_date_hour = pd.to_datetime(hour_df['dteday']).dt.date.min()
max_date_hour = pd.to_datetime(hour_df['dteday']).dt.date.max()
start_date_hour, end_date_hour = st.sidebar.date_input(
    "Rentang Waktu (Per Jam)",
    min_value=min_date_hour,
    max_value=max_date_hour,
    value=[min_date_hour, max_date_hour]
)

# Filter data berdasarkan rentang waktu
filtered_data_day = day_df[(day_df['dteday'] >= str(start_date_day)) & (day_df['dteday'] <= str(end_date_day))]
filtered_data_hour = hour_df[(hour_df['dteday'] >= str(start_date_hour)) & (hour_df['dteday'] <= str(end_date_hour))]

# Header
st.title("Dashboard Penyewaan Sepeda")

# Section 1: Informasi Penyewaan Sepeda
st.header("Informasi Penyewaan berdasarkan tanggal yang dipilih")
st.metric("Total Penyewaan", value=filtered_data_day['cnt'].sum())
st.metric("Rata-rata Penyewaan", value=filtered_data_day['cnt'].mean())

# Section 2: Grafik Jumlah Penyewaan Bulanan
st.header("Grafik Jumlah Penyewaan Bulanan")
monthly_rent_df_day = filtered_data_day.groupby('mnth')['cnt'].sum().reset_index()
fig_monthly_day = plt.figure(figsize=(10, 6))
sns.barplot(x='mnth', y='cnt', data=monthly_rent_df_day, palette='viridis')
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penyewaan")
plt.title("Jumlah Penyewaan Bulanan (Harian)")
st.pyplot(fig_monthly_day)

# Section 3: Pengaruh Cuaca terhadap Penyewaan
st.header("Pengaruh Cuaca terhadap Penyewaan")
weather_rent_df_day = filtered_data_day.groupby('weathersit')['cnt'].sum().reset_index()
fig_weather_day = plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_rent_df_day, palette='coolwarm')
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan")
plt.title("Pengaruh Cuaca terhadap Penyewaan Harian")
st.pyplot(fig_weather_day)

# Section 4: Informasi per Jam
st.header("Informasi Penyewaan per Jam")
st.metric("Total Penyewaan per Jam", value=filtered_data_hour['cnt'].sum())
st.metric("Rata-rata Penyewaan per Jam", value=filtered_data_hour['cnt'].mean())

# Section 5: Grafik Jumlah Penyewaan per Jam
st.header("Grafik Jumlah Penyewaan per Jam")
hourly_rent_df = filtered_data_hour.groupby('hr')['cnt'].sum().reset_index()
fig_hourly = plt.figure(figsize=(10, 6))
sns.barplot(x='hr', y='cnt', data=hourly_rent_df, palette='mako')
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")
plt.title("Jumlah Penyewaan per Jam")
st.pyplot(fig_hourly)

# Footer
st.caption('Copyright (c) Muhammad Khairul Rizki Ramadhan 2023')
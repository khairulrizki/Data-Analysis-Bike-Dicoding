# Dashboard Penyewaan Sepeda - Final Project Data Analysis

Ini adalah dashboard sederhana untuk visualisasi data penyewaan sepeda. Dashboard ini dibangun menggunakan Streamlit dan memberikan wawasan tentang penyewaan sepeda harian dan per jam. Ini mencakup informasi tentang total penyewaan, rata-rata penyewaan, penyewaan bulanan, dampak cuaca terhadap penyewaan harian, dan penyewaan per jam.

## Data

Dashboard ini menggunakan dua set data: `day.csv` untuk data penyewaan sepeda harian dan `hour.csv` untuk data penyewaan sepeda per jam. Data ini mencakup berbagai fitur seperti tanggal, musim, kondisi cuaca, dan jumlah penyewaan sepeda.

## Memulai

Untuk menjalankan dashboard secara lokal, ikuti langkah-langkah berikut:

#### Menjalankan notebook.ipynb
1. Download ZIP lalu ekstrak
2. Struktur file akan terlihat seperti berikut
```
.
├── dashboard
│   ├── dashboard.py
│   └── day.csv
├── data
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── screenshots
|   ├── SS 1.png
|   ├── SS 2.png
|   ├── SS 3.png
├── README.md
├── notebook.ipynb
└── requirements.txt
```

3. Buka notebook.ipynb dan jalankan pada Jupyter notebook
4. Jalankan tiap cell nya.

#### Menjalankan dashboard.py
1. Buka dashboard.py
2. Instal Streamlit di terminal atau command prompt Anda menggunakan pip install streamlit. Instal pustaka lain seperti pandas, numpy, scipy, matplotlib, dan seaborn jika Anda belum melakukannya.
3. Harap dicatat, jangan pindahkan file csv karena berfungsi sebagai sumber data. Simpan dalam satu folder bersama dengan dashboard.py.
4. Buka VSCode Anda dan jalankan file dengan mengklik terminal dan tulis streamlit run dashboard.py.

## Fitur
Filter berdasarkan Tanggal: Gunakan sidebar untuk menyaring data berdasarkan rentang tanggal untuk penyewaan harian dan per jam.

Metrik Informatif: Dapatkan wawasan tentang total penyewaan harian, rata-rata penyewaan harian, total penyewaan per jam, dan rata-rata penyewaan per jam.

Grafik Penyewaan Bulanan: Visualisasikan jumlah total penyewaan sepeda secara bulanan.

Pengaruh Cuaca: Pahami dampak kondisi cuaca yang berbeda terhadap penyewaan sepeda harian.

Grafik Penyewaan Per Jam: Jelajahi distribusi penyewaan sepeda sepanjang hari.


# 🚴‍♂️ Analisis Data Pengguna Sepeda

## 📌 Tujuan dan Pertanyaan Bisnis

Analisis ini bertujuan untuk menggali wawasan dari data penyewaan sepeda dan menjawab pertanyaan bisnis berikut:

1. ⏰ **Bagaimana pengaruh jam dalam sehari terhadap jumlah penyewaan sepeda?**
2. 🌤️ **Apakah ada perbedaan jumlah penyewaan sepeda berdasarkan jenis cuaca (cerah, mendung, hujan, dsb)?**
3. 👥 **Apakah terdapat tren penggunaan sepeda yang berbeda antara pengguna musiman (_casual_) dan pengguna harian (_registered_)?**

---

## 📂 Dataset

📊 Dataset yang digunakan berasal dari file `day.csv` dan `hour.csv` yang berisi data penyewaan sepeda secara harian dan per jam. Fitur-fitur penting yang tersedia dalam dataset ini meliputi:

- 📅 Tanggal
- 🌦️ Musim dan Cuaca
- 🎌 Hari Libur dan Hari Kerja
- 🧍‍♂️ Jumlah Pengguna Casual dan Registered
- 🚲 Total Jumlah Penyewaan

---

## 🛠️ Tools dan Library

Analisis dilakukan menggunakan bahasa pemrograman Python dengan bantuan library berikut:

- `pandas` → manipulasi dan analisis data
- `numpy` → operasi numerik
- `matplotlib` dan `seaborn` → visualisasi data

---

## 📈 Ringkasan Hasil Analisis

### ⏰ 1. Pengaruh Jam dalam Sehari terhadap Penyewaan
- Terdapat **dua puncak penyewaan**: pagi (07.00–09.00) dan sore (16.00–18.00).
- Didominasi oleh pengguna harian (_registered_), yang menggunakan sepeda sebagai transportasi ke/dari tempat kerja.

### 🌧️ 2. Perbedaan Berdasarkan Cuaca
- **Cuaca cerah atau berawan ringan** meningkatkan jumlah penyewaan.
- **Cuaca ekstrem seperti hujan atau salju** menurunkan jumlah penyewaan secara signifikan, terutama dari pengguna casual.

### 👤 3. Perbedaan Tren Pengguna Casual vs Registered
- **Casual** → Lebih aktif saat akhir pekan dan siang hari (rekreasi).
- **Registered** → Konsisten sepanjang hari kerja dan jam sibuk (transportasi harian).

---

## 📌 Kesimpulan

🎯 Dengan memahami pola penggunaan berdasarkan waktu, cuaca, dan jenis pengguna, pihak pengelola dapat:
- Mengatur distribusi sepeda dengan lebih efisien.
- Menyesuaikan promosi atau layanan berdasarkan segmen pengguna.
- Memprediksi kebutuhan sepeda secara lebih akurat sesuai kondisi eksternal.

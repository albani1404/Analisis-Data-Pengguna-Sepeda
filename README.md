🚴‍♂️ Analisis Data Pengguna Sepeda
📌 Pertanyaan Bisnis
Analisis ini dilakukan untuk menjawab tiga pertanyaan utama terkait perilaku pengguna penyewaan sepeda:

⏰ Bagaimana pengaruh jam dalam sehari terhadap jumlah penyewaan sepeda?

🌤️ Apakah ada perbedaan jumlah penyewaan sepeda berdasarkan jenis cuaca (cerah, mendung, hujan, dsb)?

👥 Apakah terdapat tren penggunaan sepeda yang berbeda antara pengguna musiman (casual) dan pengguna harian (registered)?

📊 Dataset
Dataset yang digunakan berasal dari file day.csv dan hour.csv yang merekam data penyewaan sepeda secara harian dan per jam, lengkap dengan fitur-fitur seperti:

Tanggal

Musim dan cuaca

Hari libur dan hari kerja

Jumlah pengguna casual dan registered

Total penyewaan sepeda

🔧 Tools dan Library
Analisis dilakukan menggunakan bahasa Python dengan beberapa library berikut:

pandas untuk manipulasi data

numpy untuk perhitungan numerik

matplotlib dan seaborn untuk visualisasi

📈 Hasil Analisis
1. ⏰ Pengaruh Jam dalam Sehari
Data hour.csv menunjukkan pola dua puncak penyewaan pada pukul 07.00–09.00 dan 16.00–18.00.

Pola ini menunjukkan aktivitas perjalanan kerja, terutama pada hari kerja oleh pengguna registered.

2. 🌧️ Pengaruh Cuaca
Pada cuaca cerah atau berawan ringan, jumlah penyewaan sepeda tinggi.

Saat hujan atau salju, penyewaan menurun drastis.

Cuaca memiliki dampak langsung terhadap keputusan pengguna untuk menyewa sepeda, terutama pengguna casual.

3. 👤 Perbedaan Casual vs Registered
Casual: Lebih banyak menyewa saat akhir pekan dan siang hari → Rekreasi.

Registered: Dominan pada hari kerja dan jam sibuk → Transportasi rutin.

Terdapat tren penggunaan yang berbeda yang dapat dimanfaatkan untuk strategi layanan atau pemasaran.

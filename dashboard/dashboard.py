import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")

# Fungsi untuk load data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/all_data.csv')
    if 'dteday' in df.columns:
        df['dteday'] = pd.to_datetime(df['dteday'])
    return df

# Sidebar sebagai Navbar
st.sidebar.title("🚲 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman",
    ["Beranda", "Analisis Jam", "Analisis Cuaca", "Pengguna", "Filter Tanggal"]
)

# Load data
try:
    hour = load_data()

    st.markdown("<h2 style='color:#4a4a4a;'>📊 Dashboard Analisis Penyewaan Sepeda</h2>", unsafe_allow_html=True)

    if menu == "Beranda":
        st.subheader("Selamat datang di Dashboard Penyewaan Sepeda")
        st.markdown("""
            Aplikasi ini membantu menganalisis data penyewaan sepeda berdasarkan:
            - Jam dalam sehari
            - Kondisi cuaca
            - Jenis pengguna (casual vs registered)
            - Rentang waktu tertentu
        """)

    elif menu == "Analisis Jam":
        st.subheader('Pengaruh Jam dalam Sehari terhadap Jumlah Penyewaan Sepeda')

        if 'hr' in hour.columns and 'cnt' in hour.columns:
            hourly_rental = hour.groupby('hr')['cnt'].sum().reset_index()

            fig, ax = plt.subplots(figsize=(7, 3))
            ax.bar(hourly_rental['hr'], hourly_rental['cnt'])
            ax.set_xlabel('Jam')
            ax.set_ylabel('Jumlah Penyewaan')
            ax.set_title('Pengaruh Jam dalam Sehari terhadap Jumlah Penyewaan Sepeda')
            ax.set_xticks(range(24))
            ax.grid(True)

            st.pyplot(fig)
        else:
            st.warning("Kolom 'hr' atau 'cnt' tidak ditemukan.")

    elif menu == "Analisis Cuaca":
        st.subheader('Perbedaan Jumlah Penyewaan Sepeda Berdasarkan Jenis Cuaca')

        if 'weathersit_x' in hour.columns and 'cnt' in hour.columns:
            weather_rental = hour.groupby('weathersit_x')['cnt'].sum().reset_index()

            fig, ax = plt.subplots(figsize=(5, 3))
            sns.barplot(x='weathersit_x', y='cnt', data=weather_rental, ax=ax)
            ax.set_xlabel('Jenis Cuaca')
            ax.set_ylabel('Jumlah Penyewaan')
            ax.set_title('Penyewaan Sepeda Berdasarkan Jenis Cuaca')

            st.pyplot(fig)
        else:
            st.warning("Kolom 'weathersit_x' atau 'cnt' tidak ditemukan.")

    elif menu == "Pengguna":
        st.subheader('Tren Penggunaan Sepeda antara Pengguna Musiman dan Harian')

        if 'dteday' in hour.columns and 'casual' in hour.columns and 'registered' in hour.columns:
            user_type_rental = hour.groupby('dteday')[['casual', 'registered']].sum().reset_index()

            fig, ax = plt.subplots(figsize=(7, 3))
            ax.plot(user_type_rental['dteday'], user_type_rental['casual'], label='Casual')
            ax.plot(user_type_rental['dteday'], user_type_rental['registered'], label='Registered')
            ax.set_xlabel('Tanggal')
            ax.set_ylabel('Jumlah Penyewaan')
            ax.set_title('Penggunaan Sepeda: Casual vs Registered')
            ax.legend()

            st.pyplot(fig)
        else:
            st.warning("Kolom 'dteday', 'casual', atau 'registered' tidak ditemukan.")

    elif menu == "Filter Tanggal":
        st.subheader('Filter Data berdasarkan Rentang Tanggal')

        if 'dteday' in hour.columns:
            date_range = st.date_input(
                "Pilih rentang tanggal",
                [hour['dteday'].min(), hour['dteday'].max()],
                min_value=hour['dteday'].min().to_pydatetime(),
                max_value=hour['dteday'].max().to_pydatetime()
            )
            if len(date_range) == 2:
                start_date, end_date = date_range
                filtered_df = hour[(hour['dteday'].dt.date >= start_date) & (hour['dteday'].dt.date <= end_date)]
                st.write(f"Data dari {start_date} sampai {end_date}")
                st.dataframe(filtered_df)
        else:
            st.warning("Kolom 'dteday' tidak ditemukan.")

except Exception as e:
    st.error(f"Terjadi kesalahan saat memproses file: {e}")
    
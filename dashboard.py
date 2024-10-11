import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_data_path = 'C:/dicoding/belajar analisis data dengan Python/Bike-sharing-dataset/day.csv'
hour_data_path = 'C:/dicoding/belajar analisis data dengan Python/Bike-sharing-dataset/hour.csv'

# Reading dataset
day_df = pd.read_csv(day_data_path)
hour_df = pd.read_csv(hour_data_path)

# Memberi label pada kolom weathersit
weather_conditions = {
    1: "Clear, Few clouds",
    2: "Mist, Cloudy",
    3: "Light Snow, Light Rain",
    4: "Heavy Rain, Snow"
}

# Memberi label weathersit pada 2 dataset (day dan hour)
day_df['weathersit_label'] = day_df['weathersit'].map(weather_conditions)
hour_df['weathersit_label'] = hour_df['weathersit'].map(weather_conditions)

# Streamlit layout
st.title("Bike Sharing Analysis Dashboard")

# Pertanyaan 1: average penyewaan sepeda berdasarkan kondisi cuaca
st.header("Average Bike Rentals Based on Weather Conditions")
avg_rentals_weather = day_df.groupby('weathersit_label')['cnt'].mean()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_rentals_weather.index, y=avg_rentals_weather.values, ax=ax1)
ax1.set_title('Average Bike Rentals Under Different Weather Conditions')
ax1.set_ylabel('Average Rental Count')
ax1.set_xlabel('Weather Condition')
plt.xticks(rotation=45)
st.pyplot(fig1)


st.write("Interprtasi: Cuaca cerah/sedikit berawan menghasilkan jumlah penyewaan sepeda tertinggi, sementara kondisi salju ringan/hujan ringan menghasilkan jumlah penyewaan sepeda terendah")
st.write("")


# Pertanyaan 2: pola penyewaan sepeda di berbagai musim dan jam
st.header("Bike Rental Patterns Across Seasons and Hours")

hourly_pattern = hour_df.groupby(['season', 'hr'])['cnt'].mean().unstack()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.heatmap(hourly_pattern, cmap="Blues", ax=ax2)
ax2.set_title('Bike Rental Patterns Across Seasons and Hours')
ax2.set_ylabel('Season')
ax2.set_xlabel('Hour of the Day')
st.pyplot(fig2)

st.write("Interpretasi: Peta ini menyoroti jam-jam puncak penyewaan, yang biasanya di pagi hari dan sore hari selama musim panas dan gugur. Harga sewa umumnya lebih rendah selama musim dingin, dengan jam-jam puncak yang lebih sedikit.")
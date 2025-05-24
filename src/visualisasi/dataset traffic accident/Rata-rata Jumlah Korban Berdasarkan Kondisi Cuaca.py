import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset-Lidia-2024.xlsx", sheet_name="Dataset 1 2024")

# Bagi injuries_total dengan 10 untuk mendapatkan jumlah korban yang sesungguhnya
df['injuries_total'] = df['injuries_total'] / 10

# Hitung jumlah kecelakaan per kondisi cuaca
weather_counts = df.groupby('weather_condition')['injuries_total'].mean().sort_values(ascending=False)

# Plot
plt.figure(figsize=(10, 6))
weather_counts.plot(kind='bar', color='lightgreen')
plt.title('Rata-rata Jumlah Korban Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Korban')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Simpan sebagai JPG
plt.savefig("rata_rata_korban_per_cuaca.jpg", format='jpg', dpi=300)

# Tampilkan plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset-Lidia-2024.xlsx", sheet_name="Dataset 1 2024")

# Parsing kolom 'Date' dengan format dd/mm/yyyy
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Ekstrak bulan dan tahun
df['Month'] = df['Date'].dt.to_period('M')

# Hitung jumlah kecelakaan per bulan dan konversi index ke datetime
monthly_counts = df['Month'].value_counts().sort_index()
monthly_counts.index = monthly_counts.index.to_timestamp()

# Plot line chart
plt.figure(figsize=(10, 6))
plt.plot(monthly_counts.index, monthly_counts.values, marker='o', linestyle='-', color='teal')
plt.title('Jumlah Kecelakaan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Kecelakaan')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Simpan sebagai JPG
plt.savefig("jumlah_kecelakaan_per_bulan.jpg", format='jpg', dpi=300)

# Tampilkan grafik
plt.show()

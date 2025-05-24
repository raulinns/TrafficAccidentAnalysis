import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Dataset-Lidia-2024.xlsx', sheet_name='Dataset 2 2024')
weather_counts = df['Weather Description'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
weather_counts.plot(kind='bar', color='skyblue')
plt.title('Jumlah Kecelakaan Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Kecelakaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("jumlah_kecelakaan_per_cuaca.jpg", dpi=300)
plt.show()
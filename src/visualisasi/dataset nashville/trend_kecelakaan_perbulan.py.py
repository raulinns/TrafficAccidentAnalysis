import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load data
df = pd.read_excel('Dataset-Lidia-2024.xlsx', sheet_name='Dataset 2 2024')

# 1. Pastikan ada kolom tanggal (contoh: 'Tanggal' atau 'Date')
#    Jika format berbeda, sesuaikan contoh berikut:
df['Date'] = pd.to_datetime(df['Date'])  # Ganti 'Tanggal' dengan nama kolom di dataset Anda
df['Bulan'] = df['Date'].dt.to_period('M')  # Ekstrak bulan

# 2. Hitung kecelakaan per bulan
monthly_counts = df.groupby('Bulan').size().reset_index(name='Jumlah Kecelakaan')
monthly_counts['Bulan'] = monthly_counts['Bulan'].dt.strftime('%b %Y')  # Format: Jan 2024, Feb 2024, dst.

# 3. Urutkan berdasarkan bulan kronologis
month_order = ['Jan 2024', 'Feb 2024', 'Mar 2024', 'Apr 2024', 'May 2024', 
               'Jun 2024', 'Jul 2024', 'Aug 2024', 'Sep 2024', 'Oct 2024', 
               'Nov 2024', 'Dec 2024']
monthly_counts['Bulan'] = pd.Categorical(monthly_counts['Bulan'], categories=month_order, ordered=True)
monthly_counts = monthly_counts.sort_values('Bulan')

# 4. Plot line graph
plt.figure(figsize=(12, 6))
plt.plot(monthly_counts['Bulan'], monthly_counts['Jumlah Kecelakaan'], 
         marker='o', color='royalblue', linewidth=2, markersize=8)

# Format plot
plt.title('Trend Kecelakaan per Bulan (2024)', fontsize=14, pad=20)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Kecelakaan', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# Tambahkan label nilai di setiap titik
for x, y in zip(monthly_counts['Bulan'], monthly_counts['Jumlah Kecelakaan']):
    plt.text(x, y+0.5, f'{y}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("trend_kecelakaan_per_bulan.jpg", dpi=300, bbox_inches='tight')
plt.show()
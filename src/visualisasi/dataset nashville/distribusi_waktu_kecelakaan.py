import pandas as pd
import matplotlib.pyplot as plt

# Baca file
file_path = r"C:\ITB\informatika\LIDIA\Dataset-Lidia-2024.xlsx"
sheet_name = "Dataset 2 2024"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Gabungkan kolom tanggal, waktu, dan keterangan AM/PM
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str) + ' ' + df['Keterangan Waktu'], errors='coerce')

# Buang baris yang gagal parsing datetime
df = df.dropna(subset=['Datetime'])

# Hitung detik dari tengah malam
df['Seconds'] = (
    df['Datetime'].dt.hour * 3600 +
    df['Datetime'].dt.minute * 60 +
    df['Datetime'].dt.second
)

# Buat sumbu X buatan: tanggal 1–12 dalam tiap bulan, lalu plot secara linear
df['Month'] = df['Datetime'].dt.month
df['Day'] = df['Datetime'].dt.day

# Filter hanya tanggal 1 sampai 12
df = df[df['Day'] <= 12]

# Sumbu X: representasikan sebagai angka float dengan format: bulan + (hari-1)/12
# Misalnya: 1 Jan = 1.0, 2 Jan = 1.083, ..., 12 Jan = 2.0, dst
df['MonthDayX'] = df['Month'] + (df['Day'] - 1) / 12

# Plot
plt.figure(figsize=(16, 6))
plt.scatter(df['MonthDayX'], df['Seconds'], s=5, alpha=0.5, color='red')

# Format sumbu X
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Format sumbu Y setiap 2 jam
ticks = [i * 3600 for i in range(0, 25, 2)]
labels = [str(i) for i in range(0, 25, 2)]
plt.yticks(ticks=ticks, labels=labels)

plt.ylim(0, 86400)
plt.ylabel("Time of Day (24h)")
plt.xlabel("Month")
plt.title("Distribusi Waktu Kecelakaan 2024 (1–12 Day Months)")
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
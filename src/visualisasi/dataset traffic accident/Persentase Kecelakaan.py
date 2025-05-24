import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset-Lidia-2024.xlsx", sheet_name="Dataset 1 2024")

# Hitung jumlah kecelakaan dan persentase
accident_counts = df['first_crash_type'].value_counts()
total = accident_counts.sum()
percentages = (accident_counts / total * 100).round(1)

# Filter kategori yang memiliki persentase >= 1%
mask = percentages >= 1.0
filtered_counts = accident_counts[mask]

# Kelompokkan kategori kecil (<1%) sebagai "Lainnya"
other_count = accident_counts[~mask].sum()
if other_count > 0:
    filtered_counts = pd.concat([filtered_counts, pd.Series({'Lainnya (<1%)': other_count})])

# Hitung ulang persentase setelah filtering
new_percentages = (filtered_counts / total * 100).round(1)

# Plot
plt.figure(figsize=(10, 8))
plt.pie(
    filtered_counts,
    labels=filtered_counts.index,
    autopct=lambda p: f'{p:.1f}%' if p >= 1.0 else '',  # Sembunyikan label <1%
    startangle=90,
    counterclock=False,
    textprops={'fontsize': 9},
    colors=plt.cm.tab20.colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}
)

plt.title('Persentase Kecelakaan (Kategori <1% Digabung sebagai "Lainnya")')
plt.tight_layout()

# Simpan sebagai JPG
plt.savefig("persentase_kecelakaan_filtered.jpg", format='jpg', dpi=300, bbox_inches='tight')
plt.show()
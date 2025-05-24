import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

# Konfigurasi gaya plot
rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10
})

# Konfigurasi file
file_path = r"C:\ITB\informatika\LIDIA\Dataset-Lidia-2024.xlsx"
sheet_name = "Dataset 2 2024"
target_column = "Collision Type Description"

try:
    # 1. Baca dan validasi data
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File tidak ditemukan di: {file_path}")
    
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    if target_column not in df.columns:
        available_cols = ', '.join(df.columns)
        raise KeyError(f"Kolom '{target_column}' tidak ditemukan. Kolom yang tersedia: {available_cols}")

    # 2. Proses data
    collision_counts = df[target_column].value_counts()
    total_collisions = collision_counts.sum()
    
    # Gabungkan kategori kecil (<1%) dan urutkan
    threshold = 0.01 * total_collisions
    major_categories = collision_counts[collision_counts >= threshold]
    other_categories = pd.Series({'Lain-lain (<1%)': collision_counts[collision_counts < threshold].sum()})
    collision_counts_filtered = pd.concat([major_categories, other_categories]).sort_values(ascending=False)

    # 3. Warna khusus untuk kategori penting
    color_map = {
        'Front to Rear': '#4e79a7',
        'ANGLE': '#f28e2b',
        'NOT COLLISION W/MOTOR VEHICLE-TRANSPORT': '#e15759',
        'SIDESWIPE - SAME DIRECTION': '#76b7b2',
        'HEAD-ON': '#59a14f',
        'SIDESWIPE - OPPOSITE DIRECTION': '#edc948',
        'UNKNOWN': '#b07aa1',
        'Lain-lain (<1%)': '#9c755f'
    }
    colors = [color_map.get(x, '#bab0ac') for x in collision_counts_filtered.index]

    # 4. Plotting
    plt.figure(figsize=(12, 8))
    
    # Pie chart utama
    wedges, texts, autotexts = plt.pie(
        collision_counts_filtered,
        labels=None,
        autopct=lambda p: f'{p:.1f}%' if p >= 1 else '',
        startangle=90,
        colors=colors,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
        textprops={'fontsize': 10, 'fontweight': 'bold'},
        pctdistance=0.8
    )

    # 5. Legenda dan anotasi
    legend_labels = [f"{label} ({count:,})" for label, count in zip(collision_counts_filtered.index, collision_counts_filtered)]
    
    plt.legend(
        wedges,
        legend_labels,
        title="Jenis Tabrakan",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        frameon=False
    )

    # 6. Judul dan informasi tambahan
    plt.title(
        'Distribusi Jenis Tabrakan\n' + 
        r'$\bf{' + f'Total: {total_collisions:,} Kejadian' + '}$',
        pad=20,
        loc='left'
    )
    
    # Tambahkan catatan kaki
    plt.annotate(
        f"Sumber data: {os.path.basename(file_path)} | Dibuat pada: {pd.Timestamp.now().strftime('%d/%m/%Y')}",
        xy=(0.5, -0.1),
        xycoords='axes fraction',
        ha='center',
        fontsize=9,
        color='gray'
    )

    # 7. Simpan dan tampilkan
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(file_path), "distribusi_tabrakan_visual.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=False)
    print(f"Visualisasi disimpan di: {output_path}")
    
    plt.show()

except Exception as e:
    print(f"Terjadi kesalahan:\n{str(e)}")
    print("\nSolusi:")
    print("1. Pastikan file Excel ada di lokasi yang benar")
    print("2. Periksa nama sheet dan kolom")
    print("3. Tutup file Excel jika sedang terbuka")
import pandas as pd
import numpy as np

# 1. Load Data
df = pd.read_csv('nashville-accidents-2024.csv')

# 2. Statistik Deskriptif untuk Kolom Numerik
numeric_cols = [
    'Number of Motor Vehicles', 
    'Number of Injuries',
    'Number of Fatalities'
]

print("="*50)
print("STATISTIK DESKRIPTIF (KOLOM NUMERIK)")
print("="*50)

for col in numeric_cols:
    if col in df.columns:
        print(f"\n🔹 {col}:")
        stats = {
            'Rata-rata': df[col].mean(),
            'Std Deviasi': df[col].std(),
            'Min': df[col].min(),
            '10%': df[col].quantile(0.10),
            '25%': df[col].quantile(0.25),
            'Median': df[col].median(),
            '75%': df[col].quantile(0.75),
            '90%': df[col].quantile(0.90),
            'Max': df[col].max()
        }
        
        for key, value in stats.items():
            print(f"{key}: {value:.2f}")

# 3. Statistik Deskriptif untuk Kolom Kategorikal
categorical_cols = [
    'Collision Type Description',
    'Weather Description',
    'Illumination Description',
    'City',
    'Hit and Run',
    'Property Damage'
]

print("\n" + "="*50)
print("DISTRIBUSI FREKUENSI (KOLOM KATEGORIKAL)")
print("="*50)

for col in categorical_cols:
    if col in df.columns:
        print(f"\n🔹 Distribusi {col}:")
        print(df[col].value_counts(normalize=True).head(10))  # Top 10 kategori
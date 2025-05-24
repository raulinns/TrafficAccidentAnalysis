import pandas as pd
import numpy as np

# 1. Load Data
df = pd.read_csv('traffic_accidents_2024.csv')

# 2. Statistik Deskriptif untuk Kolom Numerik
numeric_cols = [
    'num_units',
    'injuries_total',
    'injuries_fatal',
    'injuries_incapacitating',
    'injuries_non_incapacitating',
    'injuries_reported_not_evident',
    'crash_hour'
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
    'traffic_control_device',
    'weather_condition',
    'lighting_condition',
    'first_crash_type',
    'roadway_surface_cond',
    'prim_contributory_cause',
    'most_severe_injury',
    'crash_day_of_week',
    'crash_month'
]

print("\n" + "="*50)
print("DISTRIBUSI FREKUENSI (KOLOM KATEGORIKAL)")
print("="*50)

for col in categorical_cols:
    if col in df.columns:
        print(f"\n🔹 Distribusi {col}:")
        print(df[col].value_counts(normalize=True).head(10))  # Top 10 kategori

# 4. Analisis Temporal
if 'crash_hour' in df.columns:
    print("\n" + "="*50)
    print("DISTRIBUSI JAM TERJADINYA KECELAKAAN")
    print("="*50)
    print(df['crash_hour'].value_counts().sort_index())

if 'crash_day_of_week' in df.columns:
    day_map = {1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 
               5: 'Jumat', 6: 'Sabtu', 7: 'Minggu'}
    print("\n" + "="*50)
    print("DISTRIBUSI HARI DALAM MINGGU")
    print("="*50)
    print(df['crash_day_of_week'].map(day_map).value_counts())
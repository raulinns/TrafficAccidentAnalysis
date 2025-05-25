import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# 1. Load data
data = pd.read_csv('../../dataset/cleaned-dataset/nashville_accidents_cleaned.csv')

# 1. Load data dan seleksi kolom
weather_injuries = data[['Weather Description', 'Number of Injuries']].copy()

# 2. Cek missing values sebelum cleaning
print("Missing values sebelum cleaning:")
print(weather_injuries.isna().sum())

# 3. Bersihkan data (drop rows dengan NaN)
weather_injuries_clean = weather_injuries.dropna()
print(f"\nJumlah data valid: {len(weather_injuries_clean)} dari total {len(data)}")

# 4. Verifikasi tidak ada NaN lagi
print("\nMissing values setelah cleaning:")
print(weather_injuries_clean.isna().sum())

# 5. Mapping untuk Weather Description
weather_mapping = {
    'UNKNOWN': 1,
	'OTHER': 2,
    'CLEAR': 3,
    'CLOUDY/OVERCAST': 4,
    'RAIN': 5,
    'SNOW': 6,
    'SLEET/HAIL': 7,
    'FOG/SMOKE/HAZE': 8,
    'BLOWING SNOW': 9,
    'FREEZING RAIN/DRIZZLE': 10

}

# 6. Tambahkan kolom encoded dan pastikan tidak ada NaN dalam mapping
weather_injuries_clean['Weather_Code'] = (
    weather_injuries_clean['Weather Description']
    .map(weather_mapping)
    .fillna(10)  # Assign nilai default untuk kategori tidak dikenal
)

# 7. Konversi ke integer
weather_injuries_clean['Weather_Code'] = weather_injuries_clean['Weather_Code'].astype(int)

# 8. Verifikasi data final
print("\n5 data pertama setelah cleaning:")
print(weather_injuries_clean.head())

# 9. Scatter Plot dengan Regresi
plt.figure(figsize=(14, 8))

# Plot semua titik data dengan jitter untuk menghindari overlap
np.random.seed(42)  # Untuk reproducibility
weather_injuries_clean['Weather_Code_jittered'] = (
    weather_injuries_clean['Weather_Code'] + 
    np.random.uniform(-0.2, 0.2, size=len(weather_injuries_clean))
)

sns.scatterplot(
    x='Weather_Code_jittered',
    y='Number of Injuries',
    data=weather_injuries_clean,
    hue='Weather Description',
    palette='viridis',
    alpha=0.6,
    s=60
)

# 10. Hitung dan plot regresi linear (gunakan nilai asli tanpa jitter)
X = weather_injuries_clean['Weather_Code'].values.reshape(-1, 1)
y = weather_injuries_clean['Number of Injuries'].values

# Verifikasi final tidak ada NaN
print("\nCek NaN terakhir di X:", np.isnan(X).any())
print("Cek NaN terakhir di y:", np.isnan(y).any())

model = LinearRegression()
model.fit(X, y)

x_range = np.linspace(min(X), max(X), 100)
y_pred = model.predict(x_range)

plt.plot(
    x_range, 
    y_pred, 
    color='red', 
    linewidth=2,
    label=f'Regresi: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}'
)

# 11. Format plot
plt.title('Hubungan Langsung antara Kondisi Cuaca dan Jumlah Cedera', fontsize=16, pad=20)
plt.xlabel('Kode Kondisi Cuaca (dengan jitter)', fontsize=12)
plt.ylabel('Jumlah Cedera', fontsize=12)
plt.xticks(ticks=list(weather_mapping.values()), 
           labels=[f"{k} ({v})" for k,v in weather_mapping.items()],
           rotation=45)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 12. Analisis statistik
X_sm = sm.add_constant(X)
model_sm = sm.OLS(y, X_sm).fit()

print("\n=== HASIL ANALISIS REGRESI ===")
print(f"Koefisien: {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R-squared: {model_sm.rsquared:.4f}")
print("\nRingkasan Statistik:")
print(model_sm.summary())

plt.show()
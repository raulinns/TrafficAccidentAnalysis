import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('DS2-nashville_accidents_2024.csv')

cols_to_drop = [
    'ObjectId', 'HarmfulCodes', 'Reporting Officer', 'x', 'y', 
    'RPA', 'Long', 'Lat', 'Zip Code', 'Precinct', 'State', 'City',
    'Property Damage'
]

df = df.drop(columns=cols_to_drop, errors='ignore')

# Identifikasi kolom kuantitatif
quant_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()


# Kolom ordinal (contoh: Property Damage dengan skala Low/Medium/High)
ordinal_cols = ['Property Damage', 'Hit and Run', 'Collision Type Description', 'Weather Description', 'Illumination Description']
ordinal_mapping = {
    'Hit and Run': {'N': 0, 'Y': 1},
    'Collision Type Description': {
		'ANGLE': 1,
		'Front to Rear': 2,
		'REAR-TO-REAR': 3,
		'Rear to Side': 4, 
        'HEAD-ON': 5,
		'SIDESWIPE - SAME DIRECTION': 6,
		'SIDESWIPE - OPPOSITE DIRECTION': 7,
		'NOT COLLISION W/MOTOR VEHICLE-TRANSPORT': 8,
		'OTHER': 9,
		'UNKNOWN': 10,
	},
    'Weather Description': {
        'CLEAR': 1,
		'CLOUDY': 2,
		'RAIN': 3, 
		'SNOW': 4,
		'FOG': 5,
		'SLEET, HAIL': 6,
		'BLOWING SAND/SOIL/DIRT': 7,
		'BLOWING SNOW': 8,
		'SEVERE CROSSWIND': 9,
		'OTHER (NARRATIVE)': 10, 
		'UNKNOWN': 11,
	},
    'Illumination Description': {
		'DAYLIGHT': 1,
		'DUSK': 2,
		'DAWN': 3,
		'DARK - LIGHTED': 4,
		'DARK - NOT LIGHTED': 5,
        'Dark-Unknown Lighting': 6,
		'OTHER': 7,
		'UNKNOWN': 8,
	}
}

# Konversi kolom ordinal ke numerik
for col in ordinal_cols:
    if col in df.columns:
        df[col+'_num'] = df[col].map(ordinal_mapping.get(col, {}))

# Gabungkan semua kolom kuantitatif
all_quant_cols = quant_cols + [col+'_num' for col in ordinal_cols if col in df.columns]

# Hitung korelasi dengan metode yang sesuai
corr_matrix = df[all_quant_cols].corr(method='spearman')  # Spearman untuk ordinal dan non-linear

# Filter hanya korelasi yang signifikan (opsional)
significant_corr = corr_matrix[(corr_matrix.abs() > 0.3) & (corr_matrix != 1.0)].dropna(how='all', axis=0).dropna(how='all', axis=1)

plt.figure(figsize=(15, 12))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Masking segitiga atas
sns.heatmap(corr_matrix, 
            mask=mask,
            annot=True, 
            fmt=".2f", 
            cmap='coolwarm',
            center=0,
            vmin=-1, 
            vmax=1,
            linewidths=0.5,
            cbar_kws={"shrink": 0.8})

plt.title('Korelasi Antar Atribut Kuantitatif (Spearman)', pad=20, fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.show()
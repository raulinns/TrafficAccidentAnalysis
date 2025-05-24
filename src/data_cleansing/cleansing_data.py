import pandas as pd

# ================================
# LOAD DATASET
# ================================
traffic_df = pd.read_csv(r"C:\Users\sabeink\Downloads\traffic_accidents_2024.csv")
nashville_df = pd.read_csv(r"C:\Users\sabeink\Downloads\nashville-accidents-2024.csv")

# Membersihkan nama kolom dataset Nashville (menghindari spasi ganda & newline)
nashville_df.columns = [col.strip().replace('\n', ' ').replace('  ', ' ') for col in nashville_df.columns]

# ================================
# TRAFFIC ACCIDENTS 2024 CLEANSING
# ================================
df_clean_traffic = traffic_df.copy()

# 1. Ganti 'UNKNOWN' pada kolom kategorikal dengan modus
for col in ['weather_condition', 'lighting_condition']:
    mode_val = df_clean_traffic[col][df_clean_traffic[col].str.upper() != 'UNKNOWN'].mode()[0]
    df_clean_traffic[col] = df_clean_traffic[col].replace('UNKNOWN', mode_val)

# 2. Hapus outlier pada 'injuries_total' dan 'num_units' menggunakan metode IQR
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df_clean_traffic = remove_outliers_iqr(df_clean_traffic, 'injuries_total')
df_clean_traffic = remove_outliers_iqr(df_clean_traffic, 'num_units')

# 3. Simpan dataset hasil cleansing
df_clean_traffic.to_csv("traffic_accidents_cleaned.csv", index=False)
print("✔ Data Traffic Accidents berhasil dibersihkan dan disimpan ke 'traffic_accidents_cleaned.csv'")

# ================================
# NASHVILLE ACCIDENTS 2024 CLEANSING
# ================================
df_clean_nashville = nashville_df.copy()

# 1. Isi nilai kosong pada kategori dengan modus
for col in ['Weather Description', 'Illumination Description', 'Collision Type Description']:
    mode_val = df_clean_nashville[col].mode()[0]
    df_clean_nashville[col] = df_clean_nashville[col].fillna(mode_val)

# 2. Tidak ada outlier signifikan → tidak dilakukan penghapusan

# 3. Simpan dataset hasil cleansing
df_clean_nashville.to_csv("nashville_accidents_cleaned.csv", index=False)
print("✔ Data Nashville Accidents berhasil dibersihkan dan disimpan ke 'nashville_accidents_cleaned.csv'")
import pandas as pd

# Load datasets
traffic_df = pd.read_csv(r"C:\Users\sabeink\Downloads\traffic_accidents_2024.csv")
nashville_df = pd.read_csv(r"C:\Users\sabeink\Downloads\nashville-accidents-2024.csv")

# Membersihkan nama kolom dataset Nashville (menghindari spasi dan newline)
nashville_df.columns = [col.strip().replace('\n', ' ').replace('  ', ' ') for col in nashville_df.columns]

# --- CEK KOTORAN DATA ---

print("=== TRAFFIC ACCIDENTS 2024 ===")
# 1. Nilai UNKNOWN pada kategori
print("Jumlah 'UNKNOWN' pada weather_condition:", (traffic_df['weather_condition'].str.upper() == 'UNKNOWN').sum())
print("Jumlah 'UNKNOWN' pada lighting_condition:", (traffic_df['lighting_condition'].str.upper() == 'UNKNOWN').sum())

# 2. Outlier numerik
print("Jumlah outlier pada injuries_total (>10):", (traffic_df['injuries_total'] > 10).sum())
print("Jumlah outlier pada num_units (>10):", (traffic_df['num_units'] > 10).sum())

# 3. Missing pada first_crash_type dan parsed_datetime
print("Missing pada first_crash_type:", traffic_df['first_crash_type'].isna().sum())
print("Missing pada parsed_datetime:", traffic_df['parsed_datetime'].isna().sum())

print("\n=== NASHVILLE ACCIDENTS 2024 ===")
# 1. Nilai kosong pada variabel kategori
print("Missing pada Weather Description:", nashville_df['Weather Description'].isna().sum())
print("Missing pada Illumination Description:", nashville_df['Illumination Description'].isna().sum())
print("Missing pada Collision Type Description:", nashville_df['Collision Type Description'].isna().sum())

# 2. Outlier numerik
print("Outlier Number of Injuries > 10:", (nashville_df['Number of Injuries'] > 10).sum())
print("Outlier Number of Motor Vehicles > 10:", (nashville_df['Number of Motor Vehicles'] > 10).sum())

# 3. Missing pada Date and Time
print("Missing pada Date and Time:", nashville_df['Date and Time'].isna().sum())
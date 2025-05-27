import pandas as pd

df = pd.read_csv('DS1-traffic_accidents.csv')

for col in df.select_dtypes(include=['object']).columns:
    print(f"\nNilai unik kolom '{col}':")
    print(df[col].value_counts())
import pandas as pd

df = pd.read_csv('../../dataset/DS2-nashville_accidents_2024.csv')

for col in df.select_dtypes(include=['object']).columns:
    print(f"\nNilai unik kolom '{col}':")
    print(df[col].value_counts())
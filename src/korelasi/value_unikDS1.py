import pandas as pd

df = pd.read_csv('../../dataset/cleaned-dataset/nashville_accidents_cleaned.csv')

for col in df.select_dtypes(include=['object']).columns:
    print(f"\nNilai unik kolom '{col}':")
    print(df[col].value_counts())
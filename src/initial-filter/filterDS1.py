import pandas as pd
import os

# 1. Load your CSV file
input_path = r"C:\00-IMPORTANT\01-ITB\01-IF-2024\02-Semester-2\06-Literasi-Data-dan-Inteligensi-Artifisial\02-Tugas\Tubes\traffic_accidents.csv"
try:
    df = pd.read_csv(input_path)
    print("Original data loaded successfully. Columns:", df.columns.tolist())
except Exception as e:
    print(f"Error loading {input_path}: {str(e)}")
    exit()

# 2. Auto-detect datetime column (case-insensitive)
datetime_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
if not datetime_cols:
    print("Error: No datetime column found. Available columns:", df.columns.tolist())
    exit()

datetime_col = datetime_cols[0]
print(f"Using column '{datetime_col}' for datetime operations")

# 3. Parse datetime with validation
df['parsed_datetime'] = pd.to_datetime(
    df[datetime_col],
    format='%m/%d/%Y %I:%M:%S %p',  # Format for "10/30/2024 07:50:00 AM"
    errors='coerce'
)

# 4. Check for parsing errors
na_count = df['parsed_datetime'].isna().sum()
if na_count > 0:
    print(f"Warning: {na_count} rows failed datetime parsing. Examples:")
    print(df[df['parsed_datetime'].isna()][datetime_col].head(3))

# 5. Split into date and time components
df['date'] = df['parsed_datetime'].dt.date
df['time'] = df['parsed_datetime'].dt.time

# 6. Filter for 2024 only
df_2024 = df[df['parsed_datetime'].dt.year == 2024].copy()
print(f"\nFiltered to {len(df_2024)} rows from 2024")
print("Date range:", df_2024['parsed_datetime'].min().date(), "to", df_2024['parsed_datetime'].max().date())

# 7. Save the processed data
output_path = r"C:\00-IMPORTANT\01-ITB\01-IF-2024\02-Semester-2\06-Literasi-Data-dan-Inteligensi-Artifisial\02-Tugas\Tubes\traffic_accidents_2024.csv"
try:
    df_2024.to_csv(
        output_path,
        index=False,
        encoding='utf-8-sig',  # Best compatibility for VSCode/Excel
        date_format='%m/%d/%Y'  # Consistent date formatting
    )
    print(f"\nSuccess! Saved 2024 data to:\n{output_path}")
    
    # Verify the saved file
    if os.path.exists(output_path):
        print("\nFile verification:")
        with open(output_path, 'r', encoding='utf-8-sig') as f:
            print("First line:", f.readline().strip())
        test_df = pd.read_csv(output_path)
        print(f"Loaded back {len(test_df)} rows")
        print(df_2024.info())  # Descriptive info about the DataFrame
        print(df_2024.shape)  # gives a tuple with the shape of DataFrame

    else:
        print("Error: File not created")
        
except Exception as e:
    print(f"\nError saving file: {str(e)}")
    print("Trying alternative save method...")
    df_2024.to_csv(output_path, index=False, encoding='utf-8')  # Fallback
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_excel("Dataset-Lidia-2024.xlsx", sheet_name="Dataset 1 2024")
df['crash_date'] = pd.to_datetime(df['crash_date'], format="%m/%d/%Y %I:%M:%S %p")

# Create synthetic 12-day months
df['month'] = df['crash_date'].dt.month
df['day_in_month'] = np.clip(df['crash_date'].dt.day, 1, 12)  # Clamp days to 1-12
df['synthetic_date'] = df['month'] + (df['day_in_month']-1)/12  # Convert to continuous 12-day months

# Time calculation
df['time_decimal'] = df['crash_date'].dt.hour + df['crash_date'].dt.minute/60

# Plot
plt.figure(figsize=(20, 8))
plt.scatter(
    df['synthetic_date'], 
    df['time_decimal'],
    alpha=0.4,
    s=10,
    color='darkblue',
    edgecolors='none'
)

# X-axis formatting
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(
    ticks=np.arange(1, 13),
    labels=months,
    fontsize=12
)

# Y-axis formatting
plt.ylim(0, 24)
plt.yticks(np.arange(0, 25, 2))
plt.ylabel("Time of Day (24h)", fontweight='bold', fontsize=12)

# Grid and styling
plt.grid(True, alpha=0.3)
plt.title("Crash Time Distribution 2024 (12-Day Months)", 
          fontsize=14, pad=20, fontweight='bold')

plt.tight_layout()
plt.savefig("12day_month_crash_times.jpg", dpi=300, bbox_inches='tight')
plt.show()

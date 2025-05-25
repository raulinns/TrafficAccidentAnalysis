import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, pointbiserialr, chi2_contingency, f_oneway

# 1. Load Data
df = pd.read_csv('../../dataset/2024-dataset/DS1-traffic_accidents_2024.csv')

# 2. Preprocessing
cols_to_drop = [
    'ObjectId', 'HarmfulCodes', 'Reporting Officer', 'x', 'y', 
    'RPA', 'Long', 'Lat', 'Zip Code', 'Precinct', 'State', 'City',
    'Property Damage'
]
df = df.drop(columns=cols_to_drop, errors='ignore')

# 3. Define Column Types
numerik_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
kategorikal_biner = ['intersection_related_i', ]
kategorikal_multi = ['Collision Type Description', 'Weather Description', 'Illumination Description']

# 4. Ordinal Mapping (same as before)
ordinal_mapping = {
    'intersection_related_i': {'N': 0, 'Y': 1},
    'traffic_control_device': {
        'UNKNOWN': 1,
    	'OTHER': 2,
    	'NO CONTROLS': 3,
    	'YIELD': 4,
    	'TRAFFIC SIGNAL': 5,
    	'PEDESTRIAN CROSSING SIGN': 6,
    	'STOP SIGN/FLASHER': 7,
    	'FLASHING CONTROL SIGNAL': 8,
		'OTHER REG. SIGN': 9,
		'POLICE/FLAGMAN': 10,
		'SCHOOL ZONE': 11,
		'RR CROSSING SIGN': 12,
		'RAILROAD CROSSING GATE': 13,
		'OTHER RAILROAD CROSSING': 14,
		'BICYCLE CROSSING SIGN': 15,
		'DELINEATORS': 16,
		'NO PASSING': 17
	},
    'weather_condition': {
		'UNKNOWN': 1,
		'OTHER': 2,
		'CLEAR': 3,
		'CLOUDY/OVERCAST': 4,
		'RAIN': 5,
		'SNOW': 6,
		'SLEET/HAIL': 7,
		'FREEZING RAIN/DRIZZLE': 8,
		'FOG/SMOKE/HAZE': 9,
		'BLOWING SNOW': 10
	},
    'lighting_condition': {
        'UNKNOWN': 1,
		'DAYLIGHT': 2,
		'DAWN': 3,
		'DUSK': 4,
		'DARKNESS, LIGHTED ROAD': 5,
		'DARKNESS': 6
	},
    'first_crash_type': {
		'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
		'OTHER NONCOLLISION': 2,
		'OTHER OBJECT': 2,  # Treating as "OTHER"
		'SIDESWIPE SAME DIRECTION': 3,
		'REAR END': 4,
		'ANGLE': 5,
		'TURNING': 6,
		'REAR TO SIDE': 7,
		'REAR TO FRONT': 8,
		'HEAD ON': 9,
		'SIDESWIPE OPPOSITE DIRECTION': 10,
		'PARKED MOTOR VEHICLE': 11,
		'FIXED OBJECT': 12,
		'PEDESTRIAN': 13,
		'PEDALCYCLIST': 14,
		'OVERTURNED': 15,
		'ANIMAL': 16,
		'TRAIN': 17,
		'REAR TO REAR': 18
	}, 
    'trafficway_type': {
		'UNKNOWN': 1,
		'UNKNOWN INTERSECTION TYPE': 1,  # Treating as "UNKNOWN"
		'NOT REPORTED': 1,  # Treating as "UNKNOWN"
		'OTHER': 2,
		'DIVIDED - W/MEDIAN BARRIER': 3,
		'DIVIDED - W/MEDIAN (NOT RAISED)': 4,
		'FOUR WAY': 5,
		'NOT DIVIDED': 6,
		'T-INTERSECTION': 7,
		'L-INTERSECTION': 8,
		'Y-INTERSECTION': 9,
		'ONE-WAY': 10,
		'ROUNDABOUT': 11,
		'CENTER TURN LANE': 12,
		'TRAFFIC ROUTE': 13,
		'FIVE POINT, OR MORE': 14,
		'DRIVEWAY': 15,
		'ALLEY': 16,
		'PARKING LOT': 17,
		'RAMP': 18
	},
	'alignment': {
		'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
		'OTHER': 2,    # Added OTHER though not in original mapping
		'STRAIGHT AND LEVEL': 3,
		'STRAIGHT ON GRADE': 4,
		'STRAIGHT ON HILLCREST': 5,
		'CURVE, LEVEL': 6,
		'CURVE ON GRADE': 7,
		'CURVE ON HILLCREST': 8
	},
    'roadway_surface_cond':{
		'UNKNOWN': 1,
		'OTHER': 2,
		'DRY': 3,
		'WET': 4,
		'SNOW OR SLUSH': 5,
		'ICE': 6
	},

	'road_detect': {
		'UNKNOWN': 1,
		'OTHER': 2,
		'NO DEFECTS': 3,
		'DEBRIS ON ROADWAY': 4,
		'RUT, HOLES': 5,
		'SHOULDER DEFECT': 6,
		'WORN SURFACE': 7
	},

	'crash_type': {
		'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
		'NO INJURY / DRIVE AWAY': 2,
		'INJURY AND / OR TOW DUE TO CRASH': 3
	},
    
	'damage': {
		'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
		'$500 OR LESS': 2,
		'$501 - $1,500': 3,
		'OVER $1,500': 4
	},

	'most_severe_injury': {
		'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
		'NO INDICATION OF INJURY': 2,
		'REPORTED, NOT EVIDENT': 3,
		'NONINCAPACITATING INJURY': 4,
		'INCAPACITATING INJURY': 5,
		'FATAL': 6
	}
}

# 5. Convert Categorical to Numerical
for col in kategorikal_biner + kategorikal_multi:
    if col in df.columns:
        df[col+'_num'] = df[col].map(ordinal_mapping.get(col, np.nan))

# 6. Prepare All Columns
all_cols = numerik_cols + [col+'_num' for col in kategorikal_biner + kategorikal_multi if col+'_num' in df.columns]

# 7. Correlation Calculation Functions
def calculate_pearson(df, col1, col2):
    valid_data = df[[col1, col2]].dropna()
    if len(valid_data) < 2:
        return np.nan
    try:
        return pearsonr(valid_data[col1], valid_data[col2])[0]
    except Exception:
        return np.nan

def calculate_spearman(df, col1, col2):
    valid_data = df[[col1, col2]].dropna()
    if len(valid_data) < 2:
        return np.nan
    try:
        return spearmanr(valid_data[col1], valid_data[col2])[0]
    except Exception:
        return np.nan

def calculate_pointbiserial(df, binary_col, numeric_col):
    valid_data = df[[binary_col, numeric_col]].dropna()
    if len(valid_data) < 2 or len(valid_data[binary_col].unique()) < 2:
        return np.nan
    try:
        return pointbiserialr(valid_data[binary_col], valid_data[numeric_col])[0]
    except Exception:
        return np.nan

def calculate_anova_eta_squared(df, categorical_col, numeric_col):
    # Collect groups for ANOVA
    groups = []
    group_has_variation = []  # Track which groups have variation
    
    for name, group in df.groupby(categorical_col):
        if not group[numeric_col].isna().all() and len(group) > 0:
            group_data = group[numeric_col].dropna()
            if len(group_data) > 0:
                groups.append(group_data)
                # Check if this group has variation (std > 0)
                group_has_variation.append(group_data.std() > 0)
    
    # Only perform ANOVA if we have at least 2 groups with non-constant values
    if len(groups) >= 2 and not any(len(g) == 0 for g in groups) and sum(group_has_variation) >= 2:
        try:
            f, p = f_oneway(*groups)
            
            # Only proceed if F is finite
            if np.isfinite(f):
                # Calculate eta-squared
                all_values = np.concatenate(groups)
                grand_mean = np.mean(all_values)
                ss_total = sum((x - grand_mean)**2 for x in all_values)
                
                if ss_total > 0:  # Avoid division by zero
                    group_means = [np.mean(group) for group in groups]
                    group_sizes = [len(group) for group in groups]
                    ss_between = sum(size * (mean - grand_mean)**2 for size, mean in zip(group_sizes, group_means))
                    
                    eta_squared = ss_between / ss_total
                    if not np.isnan(eta_squared):
                        return eta_squared
        except Exception:
            pass
    
    return np.nan

def calculate_cramers_v(df, cat1, cat2):
    contingency = pd.crosstab(df[cat1], df[cat2])
    
    if contingency.size > 1 and 0 not in contingency.shape:
        try:
            chi2, p, _, _ = chi2_contingency(contingency)
            n = contingency.sum().sum()
            min_dim = min(contingency.shape) - 1
            
            if min_dim > 0:  # Avoid division by zero
                cramers_v = np.sqrt(chi2/(n * min_dim))
                if not np.isnan(cramers_v):
                    return cramers_v
        except Exception:
            pass
    
    return np.nan

# 8. Build Correlation Matrix
corr_matrix = pd.DataFrame(index=all_cols, columns=all_cols, dtype=float)

for i, col1 in enumerate(all_cols):
    for j, col2 in enumerate(all_cols):
        if i == j:
            corr_matrix.loc[col1, col2] = 1.0
        elif i < j:
            orig_col1 = col1.replace('_num', '') if '_num' in col1 else col1
            orig_col2 = col2.replace('_num', '') if '_num' in col2 else col2
            
            try:
                # Pearson for numerical-numerical
                if col1 in numerik_cols and col2 in numerik_cols:
                    corr = calculate_pearson(df, col1, col2)
                
                # Point-Biserial for binary-numerical (check this BEFORE Spearman)
                elif (col1 in [c+'_num' for c in kategorikal_biner] and col2 in numerik_cols):
                    corr = calculate_pointbiserial(df, col1, col2)
                elif (col2 in [c+'_num' for c in kategorikal_biner] and col1 in numerik_cols):
                    corr = calculate_pointbiserial(df, col2, col1)
                
                # ANOVA with eta-squared for multi-categorical vs numerical
                elif (col1 in [c+'_num' for c in kategorikal_multi] and col2 in numerik_cols):
                    corr = calculate_anova_eta_squared(df, col1, col2)
                elif (col2 in [c+'_num' for c in kategorikal_multi] and col1 in numerik_cols):
                    corr = calculate_anova_eta_squared(df, col2, col1)
                
                # Categorical vs categorical: Cramer's V
                elif (col1 in [c+'_num' for c in kategorikal_biner+kategorikal_multi] and 
                      col2 in [c+'_num' for c in kategorikal_biner+kategorikal_multi]):
                    # Try Cramer's V first for multi-categorical variables
                    if ((col1 in [c+'_num' for c in kategorikal_multi] or 
                         col2 in [c+'_num' for c in kategorikal_multi])):
                        corr = calculate_cramers_v(df, col1, col2)
                    # Use Spearman for binary variables
                    else:
                        corr = calculate_spearman(df, col1, col2)
                else:
                    corr = np.nan
                    
                # Set value in matrix
                corr_matrix.loc[col1, col2] = corr
                corr_matrix.loc[col2, col1] = corr  # Make matrix symmetric
                
            except Exception:
                corr_matrix.loc[col1, col2] = np.nan
                corr_matrix.loc[col2, col1] = np.nan

# 9. Handle remaining NaN values
corr_matrix = corr_matrix.astype(float)

# Fill NaN with zeros for visualization purposes
corr_matrix_vis = corr_matrix.fillna(0)

# 10. Visualization
plt.figure(figsize=(16, 14))
heatmap = sns.heatmap(
    corr_matrix_vis, 
    annot=True, 
    fmt=".2f", 
    cmap='coolwarm',
    center=0,
    vmin=-1, 
    vmax=1,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

plt.title('Hybrid Correlation Matrix\n(Pearson | Spearman | ANOVA | Point-Biserial)', 
          pad=20, fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Save figure
output_path = '../../doc/korelasi/DS1-correlation-matrix.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

plt.show()

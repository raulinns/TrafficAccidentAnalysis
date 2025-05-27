import pandas as pd

# Baca file CSV
df = pd.read_csv('nashville-accidents-2024.csv')


ordinal_mapping = {
        'Property Damage': {'N': 0, 'Y': 1},
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

# Simpan ke file baru
df.to_csv('nashville-accidents-2024-quantitative.csv', index=False)
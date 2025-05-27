import pandas as pd

# Baca file CSV
df = pd.read_csv('traffic_accidents_2024.csv')

# Mapping dictionaries (with UNKNOWN=1, OTHER=2, rest ranked from 3 onward)
traffic_control_device_mapping = {
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
}
df['traffic_control_device'] = df['traffic_control_device'].map(traffic_control_device_mapping)

weather_condition_mapping = {
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
}
df['weather_condition'] = df['weather_condition'].map(weather_condition_mapping)

lighting_condition_mapping = {
    'UNKNOWN': 1,
    'DAYLIGHT': 2,
    'DAWN': 3,
    'DUSK': 4,
    'DARKNESS, LIGHTED ROAD': 5,
    'DARKNESS': 6
}
df['lighting_condition'] = df['lighting_condition'].map(lighting_condition_mapping)

first_crash_type_mapping = {
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
}
df['first_crash_type'] = df['first_crash_type'].map(first_crash_type_mapping)

trafficway_type_mapping = {
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
}
df['trafficway_type'] = df['trafficway_type'].map(trafficway_type_mapping)

alignment_mapping = {
    'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
    'OTHER': 2,    # Added OTHER though not in original mapping
    'STRAIGHT AND LEVEL': 3,
    'STRAIGHT ON GRADE': 4,
    'STRAIGHT ON HILLCREST': 5,
    'CURVE, LEVEL': 6,
    'CURVE ON GRADE': 7,
    'CURVE ON HILLCREST': 8
}
df['alignment'] = df['alignment'].map(alignment_mapping)

roadway_surface_cond_mapping = {
    'UNKNOWN': 1,
    'OTHER': 2,
    'DRY': 3,
    'WET': 4,
    'SNOW OR SLUSH': 5,
    'ICE': 6
}
df['roadway_surface_cond'] = df['roadway_surface_cond'].map(roadway_surface_cond_mapping)

road_defect_mapping = {
    'UNKNOWN': 1,
    'OTHER': 2,
    'NO DEFECTS': 3,
    'DEBRIS ON ROADWAY': 4,
    'RUT, HOLES': 5,
    'SHOULDER DEFECT': 6,
    'WORN SURFACE': 7
}
df['road_defect'] = df['road_defect'].map(road_defect_mapping)

crash_type_mapping = {
    'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
    'NO INJURY / DRIVE AWAY': 2,
    'INJURY AND / OR TOW DUE TO CRASH': 3
}
df['crash_type'] = df['crash_type'].map(crash_type_mapping)

intersection_related_mapping = {'N': 0, 'Y': 1}
df['intersection_related_i'] = df['intersection_related_i'].map(intersection_related_mapping)

damage_mapping = {
    'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
    '$500 OR LESS': 2,
    '$501 - $1,500': 3,
    'OVER $1,500': 4
}
df['damage'] = df['damage'].map(damage_mapping)

most_severe_injury_mapping = {
    'UNKNOWN': 1,  # Added UNKNOWN though not in original mapping
    'NO INDICATION OF INJURY': 2,
    'REPORTED, NOT EVIDENT': 3,
    'NONINCAPACITATING INJURY': 4,
    'INCAPACITATING INJURY': 5,
    'FATAL': 6
}
df['most_severe_injury'] = df['most_severe_injury'].map(most_severe_injury_mapping)

# Simpan hasil
df.to_csv('traffic_accidents_2024_mappeddd.csv', index=False)
print("✅ Mapping selesai dan file disimpan sebagai 'traffic_accidents_2024_mappeddd.csv'.")
import pandas as pd

# Baca file CSV
df = pd.read_csv('traffic_accidents_2024.csv')

# Mapping dictionaries (telah diurutkan dari kondisi terbaik ke terburuk)
traffic_control_device_mapping = {
    'NO CONTROLS': 1,
    'YIELD': 2,
    'TRAFFIC SIGNAL': 3,
    'PEDESTRIAN CROSSING SIGN': 4,
    'STOP SIGN/FLASHER': 5,
    'FLASHING CONTROL SIGNAL': 6,
    'OTHER REG. SIGN': 7,
    'POLICE/FLAGMAN': 8,
    'SCHOOL ZONE': 9,
    'RR CROSSING SIGN': 10,
    'RAILROAD CROSSING GATE': 11,
    'OTHER RAILROAD CROSSING': 12,
    'BICYCLE CROSSING SIGN': 13,
    'DELINEATORS': 14,
    'NO PASSING': 15,
    'OTHER': 16,
    'UNKNOWN': 17
}
df['traffic_control_device'] = df['traffic_control_device'].map(traffic_control_device_mapping)

weather_condition_mapping = {
    'CLEAR': 1,
    'CLOUDY/OVERCAST': 2,
    'RAIN': 3,
    'SNOW': 4,
    'SLEET/HAIL': 5,
    'FREEZING RAIN/DRIZZLE': 6,
    'FOG/SMOKE/HAZE': 7,
    'BLOWING SNOW': 8,
    'OTHER': 9,
    'UNKNOWN': 10
}
df['weather_condition'] = df['weather_condition'].map(weather_condition_mapping)

lighting_condition_mapping = {
    'DAYLIGHT': 1,
    'DAWN': 2,
    'DUSK': 3,
    'DARKNESS, LIGHTED ROAD': 4,
    'DARKNESS': 5,
    'UNKNOWN': 6
}
df['lighting_condition'] = df['lighting_condition'].map(lighting_condition_mapping)

first_crash_type_mapping = {
    'SIDESWIPE SAME DIRECTION': 1,
    'REAR END': 2,
    'ANGLE': 3,
    'TURNING': 4,
    'REAR TO SIDE': 5,
    'REAR TO FRONT': 6,
    'HEAD ON': 7,
    'SIDESWIPE OPPOSITE DIRECTION': 8,
    'PARKED MOTOR VEHICLE': 9,
    'FIXED OBJECT': 10,
    'PEDESTRIAN': 11,
    'PEDALCYCLIST': 12,
    'OVERTURNED': 13,
    'ANIMAL': 14,
    'TRAIN': 15,
    'REAR TO REAR': 16,
    'OTHER OBJECT': 17,
    'OTHER NONCOLLISION': 18
}
df['first_crash_type'] = df['first_crash_type'].map(first_crash_type_mapping)

trafficway_type_mapping = {
    'DIVIDED - W/MEDIAN BARRIER': 1,
    'DIVIDED - W/MEDIAN (NOT RAISED)': 2,
    'FOUR WAY': 3,
    'NOT DIVIDED': 4,
    'T-INTERSECTION': 5,
    'L-INTERSECTION': 6,
    'Y-INTERSECTION': 7,
    'ONE-WAY': 8,
    'ROUNDABOUT': 9,
    'CENTER TURN LANE': 10,
    'TRAFFIC ROUTE': 11,
    'FIVE POINT, OR MORE': 12,
    'DRIVEWAY': 13,
    'ALLEY': 14,
    'PARKING LOT': 15,
    'RAMP': 16,
    'UNKNOWN INTERSECTION TYPE': 17,
    'NOT REPORTED': 18,
    'OTHER': 19,
    'UNKNOWN': 20
}
df['trafficway_type'] = df['trafficway_type'].map(trafficway_type_mapping)

alignment_mapping = {
    'STRAIGHT AND LEVEL': 1,
    'STRAIGHT ON GRADE': 2,
    'STRAIGHT ON HILLCREST': 3,
    'CURVE, LEVEL': 4,
    'CURVE ON GRADE': 5,
    'CURVE ON HILLCREST': 6
}
df['alignment'] = df['alignment'].map(alignment_mapping)

roadway_surface_cond_mapping = {
    'DRY': 1,
    'WET': 2,
    'SNOW OR SLUSH': 3,
    'ICE': 4,
    'OTHER': 5,
    'UNKNOWN': 6
}
df['roadway_surface_cond'] = df['roadway_surface_cond'].map(roadway_surface_cond_mapping)

road_defect_mapping = {
    'NO DEFECTS': 1,
    'DEBRIS ON ROADWAY': 2,
    'RUT, HOLES': 3,
    'SHOULDER DEFECT': 4,
    'WORN SURFACE': 5,
    'OTHER': 6,
    'UNKNOWN': 7
}
df['road_defect'] = df['road_defect'].map(road_defect_mapping)

crash_type_mapping = {
    'NO INJURY / DRIVE AWAY': 1,
    'INJURY AND / OR TOW DUE TO CRASH': 2
}
df['crash_type'] = df['crash_type'].map(crash_type_mapping)

intersection_related_mapping = {'N': 0, 'Y': 1}
df['intersection_related_i'] = df['intersection_related_i'].map(intersection_related_mapping)

damage_mapping = {
    '$500 OR LESS': 1,
    '$501 - $1,500': 2,
    'OVER $1,500': 3
}
df['damage'] = df['damage'].map(damage_mapping)

most_severe_injury_mapping = {
    'NO INDICATION OF INJURY': 0,
    'REPORTED, NOT EVIDENT': 1,
    'NONINCAPACITATING INJURY': 2,
    'INCAPACITATING INJURY': 3,
    'FATAL': 4
}
df['most_severe_injury'] = df['most_severe_injury'].map(most_severe_injury_mapping)

# Simpan hasil
df.to_csv('traffic_accidents_2024_mappeddd.csv', index=False)
print("✅ Mapping selesai dan file disimpan sebagai 'traffic_accidents_2024_mappeddd.csv'.")
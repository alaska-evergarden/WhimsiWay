# Since the direct approach to load and process the entire dataset encountered an issue, let's try an alternative strategy.
# We'll load the dataset in chunks, process each chunk to calculate the required aggregations, and then combine the results.

import pandas as pd
import geojson

# Initialize an empty DataFrame to accumulate results
hotspots_accumulated = pd.DataFrame(columns=['Start_Lat', 'Start_Lng', 'num_accidents', 'avg_severity'])

# Define a function to process each chunk
def process_chunk(chunk):
    global hotspots_accumulated
    
    # Group by latitude and longitude
    grouped = chunk.groupby(['Start_Lat', 'Start_Lng'])
    
    # Calculate the number of accidents and average severity for each group
    hotspots = grouped.agg(
        num_accidents=pd.NamedAgg(column='ID', aggfunc='count'),
        avg_severity=pd.NamedAgg(column='Severity', aggfunc='mean')
    ).reset_index()
    
    # Append the results to the accumulated DataFrame
    hotspots_accumulated = pd.concat([hotspots_accumulated, hotspots], ignore_index=True)

# Load the dataset in chunks and process each chunk
chunksize = 10000  # Adjust based on your system's memory capacity
for chunk in pd.read_csv('tx_accidents.csv', chunksize=chunksize):
    process_chunk(chunk)

# Since we processed the data in chunks, there might be duplicate groups across chunks. We'll aggregate them again.
final_hotspots = hotspots_accumulated.groupby(['Start_Lat', 'Start_Lng']).agg(
    num_accidents=pd.NamedAgg(column='num_accidents', aggfunc='sum'),
    avg_severity=pd.NamedAgg(column='avg_severity', aggfunc='mean')  # This is a simplification; consider weighting
).reset_index()

# Rename columns for final output
final_hotspots.rename(columns={'Start_Lat': 'latitude', 'Start_Lng': 'longitude'}, inplace=True)

final_hotspots.head()


def dataframe_to_geojson(df, filename):
    features = []
    for _, row in df.iterrows():
        # Create a GeoJSON feature for each row
        feature = geojson.Feature(
            geometry=geojson.Point((row['longitude'], row['latitude'])),
            properties={
                'num_accidents': row['num_accidents'],
                'avg_severity': row['avg_severity']
            }
        )
        features.append(feature)
    
    # Create a FeatureCollection with all the features
    feature_collection = geojson.FeatureCollection(features)
    
    # Write the FeatureCollection to a GeoJSON file
    with open(filename, 'w') as f:
        geojson.dump(feature_collection, f)

# Assuming final_hotspots is your DataFrame
# dataframe_to_geojson(final_hotspots, 'hotspots.geojson')
        # Increase thresholds for filtering
num_accidents_threshold = 20  # Adjust this value as needed
avg_severity_threshold = 0  # Adjust this value as needed

# Filter the final_hotspots DataFrame based on the new criteria
# filtered_final_hotspots = final_hotspots[(final_hotspots['num_accidents'] >= num_accidents_threshold) &
#                                          (final_hotspots['avg_severity'] >= avg_severity_threshold)]
city_boundaries = {
    'Houston': {'lat_min': 29.5370705, 'lat_max': 30.1103506, 'lon_min': -95.9097419, 'lon_max': -95.0120525},
    # 'Dallas': {'lat_min': 32.613216, 'lat_max': 33.0239366, 'lon_min': -97.000482, 'lon_max': -96.4636317},
    "Austin": {'lat_min': 30.06869, 'lat_max': 30.58826, 'lon_min': -98.16052, 'lon_max': -97.39767},
    # 'Austin': {'lat_min': 30.0985133, 'lat_max': 30.5166255, 'lon_min': -97.9367663, 'lon_max': -97.5605288},
    "San Antonio": {'lat_min': 29.1862572, 'lat_max': 29.7309623, 'lon_min': -98.8131865, 'lon_max': -98.2230029},
    "Dallas": {'lat_min': 32.52760, 'lat_max': 33.31050, 'lon_min': -97.62194, 'lon_max': -96.35340},
}

inside_threshold = 90
outside_threshold = 10

def is_inside_any_city(lat, lon, boundaries):
    for city, bounds in boundaries.items():
        if bounds['lat_min'] <= lat <= bounds['lat_max'] and bounds['lon_min'] <= lon <= bounds['lon_max']:
            return city
    return False

# Example application on a DataFrame (this part will be integrated into your processing logic)
def filter_accidents(row):
    inside_city = is_inside_any_city(row['latitude'], row['longitude'], city_boundaries)
    # if inside_city != False:
    #     if inside_city == "San Antonio":
    #         if row['num_accidents'] > 100:
    #             return True
    #         return False
    #     return True
    if inside_city == "San Antonio":
            if row['num_accidents'] > 50:
                return True
            return False
    if inside_city == "Dallas":
            if row['num_accidents'] > 110:
                return True
            return False
    if inside_city == "Greater Dallas":
            if row['num_accidents'] > 40:
                return True
            return False
    if inside_city == "Austin":
            if row['num_accidents'] > 85:
                return True
            return False
    if inside_city == "Houston":
            if row['num_accidents'] > 100:
                return True
            return False
    
    # if inside_city and row['num_accidents'] > inside_threshold:
    #     return True
    elif not inside_city and row['num_accidents'] > 10:
        return True
    return False


filtered_final_hotspots = final_hotspots[final_hotspots.apply(filter_accidents, axis=1)]




# Then, use the filtered_final_hotspots DataFrame in the dataframe_to_geojson function
dataframe_to_geojson(filtered_final_hotspots, 'filtered_hotspots.geojson')


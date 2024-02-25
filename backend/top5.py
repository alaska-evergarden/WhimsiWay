from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import folium
from sklearn.cluster import KMeans

def get_top_5(city):
    df = pd.read_csv('tx_accidents.csv')

    # Ensure Start_Time is a datetime type and filter for 2022 onwards
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df = df[df['Start_Time'].dt.year >= 2022]
    coordinates = df[['Start_Lat', 'Start_Lng']].values

    # Convert eps to radians for use with haversine formula, assuming eps is in kilometers
    # Example: 500 meters = 0.5 kilometers
    eps_km = 0.015  # The eps value in kilometers
    eps_rad = eps_km / 6371.0088  # Earth's radius in kilometers

    # Apply DBSCAN
    db = DBSCAN(eps=eps_rad, min_samples=10, metric='haversine', algorithm='ball_tree')
    db.fit(np.radians(coordinates))

    df['cluster'] = db.labels_

    geolocator = Nominatim(user_agent="my_application")
    location = geolocator.geocode(city, exactly_one=True)

    # Get the bounding box
    bounding_box = location.raw.get('boundingbox', [])
    lat_min, lat_max = float(bounding_box[0]), float(bounding_box[1])
    lon_min, lon_max = float(bounding_box[2]), float(bounding_box[3])

    df_filtered = df[
        (df['Start_Lat'] >= lat_min) & (df['Start_Lat'] <= lat_max) &
        (df['Start_Lng'] >= lon_min) & (df['Start_Lng'] <= lon_max)
    ]
    # Aggregate accidents by cluster label
    cluster_counts = df_filtered['cluster'].value_counts()

    # After aggregating accidents by cluster label and identifying top clusters
    top_5_clusters = cluster_counts.head(5).index.tolist()

    if len(top_5_clusters) < 5:
        # Not enough clusters, use K-Means to ensure 5 centroids
        kmeans = KMeans(n_clusters=5, random_state=0).fit(df_filtered[['Start_Lat', 'Start_Lng']].values)
        # Extract centroids
        top_5_centroids = pd.DataFrame(kmeans.cluster_centers_, columns=['Start_Lat', 'Start_Lng'])
        top_5_centroids['cluster'] = range(1, 6)  # Assigning arbitrary cluster labels
    else:
        # DBSCAN resulted in 5 or more clusters, calculate centroids of the top 5
        top_5_centroids = df_filtered[df_filtered['cluster'].isin(top_5_clusters)].groupby('cluster').agg({'Start_Lat': 'mean', 'Start_Lng': 'mean'}).reset_index()

    # Proceed with reverse geocoding and mapping as before
    top_5_addresses = []
    for _, row in top_5_centroids.iterrows():
        location = geolocator.reverse((row['Start_Lat'], row['Start_Lng']), exactly_one=True)
        address = location.address if location else "Address not found"
        top_5_addresses.append((row['cluster'], address, row['Start_Lat'], row['Start_Lng']))

    # Visualization code continues as is

    # Create a base map centered around the general area of interest
    map_center = [top_5_centroids['Start_Lat'].mean(), top_5_centroids['Start_Lng'].mean()]
    new_map = folium.Map(location=map_center, zoom_start=12)  # Adjust zoom level as needed

    # Add a marker for each of the top 5 densest clusters
    for cluster_label, address, lat, lng in top_5_addresses:
        popup = folium.Popup(address, max_width=300)
        folium.Marker(
            location=[lat, lng],
            popup=popup,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(new_map)

    # Display or save the map
    new_map.save("../frontend/public/top_5_hotspots_map.html")
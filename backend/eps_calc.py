# import pandas as pd
# from sklearn.neighbors import NearestNeighbors
# import numpy as np

# # Load the dataset
# df = pd.read_csv('tx_accidents.csv')

# # Filter for accidents from 2022 onwards
# df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
# df_2022_onwards = df[df['Start_Time'].dt.year >= 2022]

# # Select a sample of data to calculate eps for DBSCAN
# coordinates = df_2022_onwards[['Start_Lat', 'Start_Lng']].sample(n=1000, random_state=1)  # Sample size of 1000 for demonstration

# # Convert coordinates to radians for Haversine distance calculation
# coords_radians = np.radians(coordinates)

# # Use NearestNeighbors to find the distance to the nearest neighbor for each point
# nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree', metric='haversine').fit(coords_radians)
# distances, indices = nbrs.kneighbors(coords_radians)

# # Sort distances
# sorted_distances = np.sort(distances[:, 1])

# # Prepare to plot
# import matplotlib.pyplot as plt

# plt.plot(sorted_distances)
# plt.xlabel('Points')
# plt.ylabel('Distance to nearest neighbor')
# plt.title('Sorted distances to nearest neighbor')
# plt.show()

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('tx_accidents.csv')

# Filter for accidents from 2022 onwards
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df_2022_onwards = df[df['Start_Time'].dt.year >= 2022]

# Select a sample of data to calculate eps for DBSCAN
coordinates = df_2022_onwards[['Start_Lat', 'Start_Lng']].sample(n=1000, random_state=1)  # Sample size of 1000 for demonstration

# Convert coordinates to radians for Haversine distance calculation
coords_radians = np.radians(coordinates)

# Use NearestNeighbors to find the distance to the nearest neighbor for each point
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree', metric='haversine').fit(coords_radians)
distances, indices = nbrs.kneighbors(coords_radians)

# Sort distances
sorted_distances = np.sort(distances[:, 1])

# Plot
plt.plot(sorted_distances)
plt.xlabel('Points')
plt.ylabel('Distance to nearest neighbor')
plt.title('Sorted distances to nearest neighbor')
plt.show()



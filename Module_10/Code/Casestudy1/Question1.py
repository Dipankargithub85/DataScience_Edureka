import seaborn as sns
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_10\\driver-data.csv", index_col="id")
data.head()

kmeans = KMeans(n_clusters=4)

kmeans.fit(data)

print("Cluster's Center\n")
print(kmeans.cluster_centers_)

print("========================================================")
# Find count of each cluster
unique, counts = np.unique(kmeans.labels_, return_counts=True)
dict_data = dict(zip(unique, counts))
print("Count of each cluster")
print(dict_data)


# Plot the clusters
data["cluster"] = kmeans.labels_
#sns.lmplot('mean_dist_day', 'mean_over_speed_perc', data=data,hue='cluster', palette='coolwarm', height=6, aspect=1, fit_reg=False)

print("========================================================")

# Inertia is the sum of squared error for each cluster.
print("Inertia:-",kmeans.inertia_)
print("========================================================")


# Print the data
print("Data with clusters\n")
print(data)
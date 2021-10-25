from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
from sklearn import metrics


data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_10\\zoo.csv")
print(data.head())
print("=======================================================================================")
# Find Unique class types
unique_classtypes = np.unique(data["class_type"].values)

# Initialize Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=3)
predicted_values = agglo.fit_predict(data.iloc[:, 1:16])

# Accuracy Score
print("Accuracy Score")
print(metrics.accuracy_score(predicted_values, data["class_type"].values)*100)
print("=======================================================================================")

# Mean Square Error value
print("Mean Squared Error value")
print(metrics.mean_squared_error(predicted_values, data["class_type"].values))

from sklearn.neighbors import NearestNeighbors
import seaborn as sns
import pandas as pd
import math
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy

import csv
import numpy as np
import matplotlib.pyplot as plt

X = []

with open("C:/Users/mlybo/OneDrive/Desktop/group_project/node_coords.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    for row in reader:
        if row:
            X.append([str(row[0]), float(row[1]), float(row[2])])


X_array = np.asarray(X)



X_array = X_array[X_array[:, 1].astype(float) <= -30.4]

df = pd.DataFrame(X_array, columns = ['key', 'x', 'y'])
df['x'] = pd.to_numeric(df['x'])
df['y'] = pd.to_numeric(df['y'])

clusters = hierarchy.linkage(df[['x', 'y']], method="ward")


plt.figure(figsize=(8, 6))
dendrogram = hierarchy.dendrogram(clusters)
# Plotting a horizontal line based on the first biggest distance between clusters 
plt.axhline(150, color='red', linestyle='--'); 
# Plotting a horizontal line based on the second biggest distance between clusters 
plt.axhline(100, color='crimson');
plt.show()



clustering_model = AgglomerativeClustering(n_clusters=5, linkage="ward")
clustering_model.fit(df[['x', 'y']])


sns.scatterplot(data=df, x='x', y='y', hue=clustering_model.labels_, palette='PuOr').set_title('With clustering');
plt.show()

df['label'] = clustering_model.labels_
df.to_csv('node_labels.csv')
        
'''
nearest_neighbors = NearestNeighbors(n_neighbors=50)
neighbors = nearest_neighbors.fit(sqrt_X_array)
distances, indices = neighbors.kneighbors(sqrt_X_array)
distances = np.sort(distances[:,10], axis=0)
fig = plt.figure(figsize=(5, 5))
plt.plot(distances)
plt.xlabel("Points")
plt.ylabel("Distance")
plt.show()

'''

'''
keys = pd.read_csv("C:/Users/mlybo/OneDrive/Desktop/group_project/network_keys.csv", dtype={'Key':'int64'})

keys.dropna(inplace=True)

df = pd.merge(df, keys, on="Key")
print(df[df['label'] == 0])


fig = plt.figure(figsize=(10, 10))
sns.scatterplot(data=df, x='x', y='y', hue='label')
plt.show()


#use .05 or .025 as epsilon
# what do you need: sim_rank scores, cluster on entire dataset

'''

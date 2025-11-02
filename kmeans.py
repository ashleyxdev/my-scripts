import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'VAR1': [1.713, 0.180, 0.353, 0.940, 1.486, 1.266, 1.540, 0.459, 0.773],
    'VAR2': [1.586, 1.786, 1.240, 1.566, 0.759, 1.106, 0.419, 1.799, 0.186]
}

df = pd.DataFrame(data)
print('Dataset:\n', df)

plt.scatter(df['VAR1'],df['VAR2'], label='Data Points')
plt.xlabel('VAR1')
plt.ylabel('VAR2')
plt.title('Initial Data Points')
plt.legend()
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(df)

df['Cluster'] = kmeans.labels_
centroids = kmeans.cluster_centers_

new_point = [[0.906, 0.606]]
predicted_cluster = kmeans.predict(new_point)
print(f"\nPredicted cluster for VAR1=0.906, VAR2=0.606 → Cluster {predicted_cluster[0]}")

plt.scatter(df['VAR1'],df['VAR2'], label='Data Points', c=df['Cluster'], cmap='rainbow')
plt.scatter(centroids[:,0], centroids[:,1], c='black', marker='*', label='Centroids')
plt.scatter(new_point[0][0], new_point[0][1], c='green', marker='X', label='new point')
plt.xlabel('VAR1')
plt.ylabel('VAR2')
plt.title('K-Means Clustering (K=3)')
plt.legend()
plt.show()

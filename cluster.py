import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data=pd.read_csv('student_data.csv')
wcss = []
for i in range(1, 20):
    km = KMeans(n_clusters=i)
    km.fit(data[['CGPA', 'IQ']])
    wcss.append(km.inertia_)



plt.plot(range(1, 20), wcss)
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


X=data[['CGPA','IQ']].values
km = KMeans(n_clusters=10)
y= km.fit_predict(X)
plt.title('KMeans Clustering of Students')
colors = plt.cm.tab10.colors
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.scatter(X[y == 2, 0], X[y == 2, 1])
plt.scatter(X[y== 3, 0], X[y == 3, 1])
plt.scatter(X[y == 4, 0], X[y== 4, 1])
plt.scatter(X[y == 5, 0], X[y == 5, 1]) 
plt.scatter(X[y == 6, 0], X[y == 6, 1])
plt.scatter(X[y == 7, 0], X[y == 7, 1])
plt.scatter(X[y == 8, 0], X[y == 8, 1])
plt.scatter(X[y == 9, 0], X[y == 9, 1])


plt.title('KMeans Clustering of Students')
plt.show()




from sklearn.cluster import KMeans
import numpy as np

def fit(X):
    kmeans = KMeans(n_clusters=9, random_state=0).fit(X)
    return kmeans.labels_
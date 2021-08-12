from sklearn.cluster import SpectralClustering
import numpy as np

def fit(X):
    clustering = SpectralClustering(n_clusters=9, assign_labels='discretize',
                                    random_state=0).fit(X)
    return clustering.labels_


import numpy as np
from sklearn.preprocessing import OneHotEncoder

import data_interpret
import file_reader as reader

import Spectral
import kmeans
import odor_seperate
import perceptron
import decision_tree
import PCA
import random_forest

import missing_data

np.set_printoptions(suppress=True)

#One hot encoding
enc = OneHotEncoder(handle_unknown='ignore')
data = reader.main()
odorless_data, odors = odor_seperate.main(data)
transformed_data = enc.fit_transform(odorless_data)

#PCA
PCA.plot(transformed_data.toarray())
PCA_data = PCA.fit(transformed_data.toarray(), 18)

#Spectral clustering:
spectral_labels = Spectral.fit(transformed_data).astype(int)
print("Spectral cluster info:")
print(data_interpret.to_matrix(spectral_labels, data))

print("\n\n-*-*-*-*-*-*-*-*-*-*-*-\n\n")

#kmeans
kmeans_labels = kmeans.fit(transformed_data).astype(int)
print("K-Means info:")
print(data_interpret.to_matrix(kmeans_labels, data))

print("\n\n-*-*-*-*-*-*-*-*-*-*-*-\n\n")

#OPTION 2
#Perceptron

print("PERCEPTRON:")
print(perceptron.main(transformed_data, odors))

#DECISION TREE

print("\nDECISION TREE: GINI & INFO GAIN")
print(decision_tree.gini_fit(transformed_data, odors))
print(decision_tree.info_gain_fit(transformed_data, odors))

#RANDOM FOREST
print("\n RANDOM FOREST:")
print(random_forest.main(transformed_data,odors))

#PCA TRANSFORMED DATA!!

#Perceptron
print("PERCEPTRON:")
print(perceptron.main(PCA_data, odors))

#DECISION TREE

print("\nDECISION TREE: GINI & INFO GAIN")
print(decision_tree.gini_fit(PCA_data, odors))
print(decision_tree.info_gain_fit(PCA_data, odors))

print("\n RANDOM FOREST:")
print(random_forest.main(PCA_data,odors))

#PART 3 - MISSING DATA
missing_data.main(data)



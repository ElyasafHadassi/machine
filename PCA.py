from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def plot(X):
    X = z_score(X)

    pca = PCA(n_components=22)
    pca.fit(X)
    exp_var = pca.explained_variance_
    total_exp_var = np.sum(exp_var)

    arr = [[], []]

    for i in range(0, 22):
        arr[0].append(i)
        ith_tot_var = np.sum(exp_var[0:i])
        arr[1].append(ith_tot_var / total_exp_var)
    print(np.array(np.transpose(arr)))
    plt.plot(arr[0], arr[1], color="black")
    return

def z_score(X):
    x_transpose = np.transpose(X)
    z_transpose = []
    for attribute in x_transpose:
        new_att = []
        mean = np.mean(attribute)
        std = np.std(attribute, axis=0)
        if std == 0:
            continue
        for x in attribute:
            new_att.append((x - mean) / std)
        z_transpose.append(new_att)
    return np.transpose(z_transpose)

def fit(X, n):
    X = z_score(X)
    pca = PCA(n_components=n)
    pca.fit(X)
    exp_var = pca.explained_variance_
    total_exp_var = np.sum(exp_var)
    return pca.fit_transform(X)
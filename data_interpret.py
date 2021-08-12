import numpy as np


def to_matrix(labels, arr):
    amount = np.zeros((9, 9))
    for i in range(len(arr)):  # a,l,c,f,y,m,n,s,p
        if arr[i][5] == "a":
            amount[labels[i]][0] += 1
        if arr[i][5] == "c":
            amount[labels[i]][1] += 1
        if arr[i][5] == "f":
            amount[labels[i]][2] += 1
        if arr[i][5] == "l":
            amount[labels[i]][3] += 1
        if arr[i][5] == "m":
            amount[labels[i]][4] += 1
        if arr[i][5] == "n":
            amount[labels[i]][5] += 1
        if arr[i][5] == "p":
            amount[labels[i]][6] += 1
        if arr[i][5] == "s":
            amount[labels[i]][7] += 1
        if arr[i][5] == "y":
            amount[labels[i]][8] += 1
    return amount

def to_num(odors):
    new_odors = []
    for odor in odors:
        if str(odor[0]) == "a":
            new_odors.append(0)
        if str(odor[0]) == "c":
            new_odors.append(1)
        if str(odor[0]) == "f":
            new_odors.append(2)
        if str(odor[0]) == "l":
            new_odors.append(3)
        if str(odor[0]) == "m":
            new_odors.append(4)
        if str(odor[0]) == "n":
            new_odors.append(5)
        if str(odor[0]) == "p":
            new_odors.append(6)
        if str(odor[0]) == "s":
            new_odors.append(7)
        if str(odor[0]) == "y":
            new_odors.append(8)
    return new_odors


def to_num1(odors):
    new_odors = []
    for odor in odors:
        if str(odor) == "a":
            new_odors.append(0)
        if str(odor) == "c":
            new_odors.append(1)
        if str(odor) == "f":
            new_odors.append(2)
        if str(odor) == "l":
            new_odors.append(3)
        if str(odor) == "m":
            new_odors.append(4)
        if str(odor) == "n":
            new_odors.append(5)
        if str(odor) == "p":
            new_odors.append(6)
        if str(odor) == "s":
            new_odors.append(7)
        if str(odor) == "y":
            new_odors.append(8)
    return new_odors
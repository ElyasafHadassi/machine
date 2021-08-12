import numpy as np

def to_array(str):
    arr = np.array([])
    memory = ""
    for c in str:
        if c == ",":
            arr = np.append(arr, memory)
            memory = ""
        else:
            memory += c
    if memory != "":
        arr = np.append(arr, memory)
    return arr

def main():
    arr = []
    f = open("mushrooms_data.txt", "r")
    # print(f.read())
    for line in f:
        stripped_line = line.strip()
        arr.append(to_array(stripped_line))
    return arr

def missing():
    arr = []
    f = open("mushrooms_data_missing.txt", "r")
    # print(f.read())
    i = 0
    for line in f:
        stripped_line = line.strip()
        arr.append(to_array(stripped_line))
    return arr

import numpy as np


X = []

for line in open("../data/data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)

print(X)

X = np.array(X)
print(X.shape)

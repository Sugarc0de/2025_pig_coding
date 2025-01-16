# Pig and dog move to a new neighborhood and they all have different places to explore (sometimes overlapping).
# For example, pig likes to explore library, bubble tea shop, etc and dog likes to go to bookstore, and skiing.
# Given a list of x, y coordinates for pig and dog, individually. Assume they want to ride the same bus along
# these places, and change the route to run along any straight line. Dog and pig also have different walking
# speed after getting off the bus. Find a bus line that can minimize the sum of squares of time they need to walk
# to each of their locations.

import numpy as np
from numpy import linalg

pig_xy = [[0, 2], [1, 4]]
dog_xy = [[2, 1], [3, 3]]

# pig_xy = [[0, 2]]
# dog_xy = [[2, 1]]

print("pig locations: ", pig_xy)
print("dog locations: ", dog_xy)

w_pig = 1
w_dog = 0.25  # Dog is twice the speed as pig


def solve(pig_xy, dog_xy):
    X = np.concatenate((pig_xy, dog_xy))  # X: (4, 2)
    pig_w = np.array([[w_pig] * 2 for _ in range(len(pig_xy))])
    dog_w = np.array([[w_dog] * 2 for _ in range(len(dog_xy))])
    W = np.concatenate((pig_w, dog_w))  # W: (4, 2)
    # Calculate the weighted mean
    WX_mean = np.average(X, axis=0, weights=W)
    # print("WX_mean: ", WX_mean)
    # Center X:
    X = X - WX_mean
    m, n = X.shape
    # print("X: ", X)
    # Calculate the weighted covariance: 1/sum wi * X * W * X_T where W is the diag(wi)
    DW = np.diag(W[:, 0])  # (4, 4)
    covariance = 1 / np.sum(W[:, 0]) * np.transpose(X).dot(DW).dot(X)
    # print("covariance: ", covariance)
    PC, V = linalg.eig(covariance)
    print("PC: ", PC)
    max_ix = np.argmax(PC)
    print("max_ix: ", max_ix)
    V = V[:, max_ix].reshape(2, 1)
    print("V: ", V)  # V shape: (2, 1)
    print("V shape: ", V.shape)

    # Reproject the original data onto the eigenvector that corresponds to the largest PC variance.
    for x_centered in X.tolist():
        x_centered = np.array(x_centered)
        x_proj = np.dot(x_centered, V) * V.reshape(2)
        diff_x = x_centered - x_proj
        print(linalg.norm(diff_x))


print(solve(pig_xy, dog_xy))

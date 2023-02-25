"""Thie module includes some loss functions"""

import numpy as np

def hinge(z):
    if z >= 1:
        return 0
    else:
        return 1 - z

def squared_error(z):
    return (z**2) / 2


theta = np.array([0,1,2])
traning = np.array([[1,0,1], [1,1,1], [1,1,-1], [-1,1,1]])
y = np.array([[2],[2.7], [-0.7], [2]])
r = 0
for i in range(4):
    #r += hinge(y[i] - np.dot(traning[i], theta))
    #print (np.dot(traning[i], theta), y[i])
    r += squared_error(y[i] - np.dot(traning[i], theta))
print (r / 4)


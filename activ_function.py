
import numpy as np 
import sys

def sigmoid(x):

    return np.exp(x) / (1 + np.exp(x))


if __name__ == "__main__":
    args = sys.argv[1]

    print (args)
    print (sigmoid(float(args)))
    


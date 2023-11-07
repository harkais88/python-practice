#!/usr/bin/python3

"""Write a NumPy program to create a one-dimensional array of forty 
pseudo-randomly generated values. Select random numbers from a uniform distribution between 0 and 1. """

import numpy as np

if __name__ == "__main__":
    # We can set the set to be specific, so it would always roll out the same generated values
    np.random.seed(10)
    arr = np.random.random(40)
    print("1-D Array of 40 pseudo-randomly generated values:\n",arr)
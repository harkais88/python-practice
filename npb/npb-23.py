#!/usr/bin/python3

"""Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.randint(0,10,5)
    print("Vector of length 10 from 0 to 10: ",arr)
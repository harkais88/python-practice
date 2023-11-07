#!/usr/bin/python3

"""Write a NumPy program to create a 3x3x3 array filled with arbitrary values."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.random((3,3,3))
    print("3x3x3 array with arbitary values:\n",arr)
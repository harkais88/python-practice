#!/usr/bin/python3

"""Write a NumPy program to sort a given array by row and column in ascending order."""

import numpy as np

if __name__ == "__main__":
    np.random.seed(10)
    arr = np.random.randint(1,50,16).reshape((4,4))
    print("Original array:\n",arr)
    print("After sorting by row:\n",np.sort(arr))
    print("After sorting by column:\n",np.sort(arr,axis=0))
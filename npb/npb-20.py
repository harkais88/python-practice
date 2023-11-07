#!/usr/bin/python3

"""Write a NumPy program to create a 3X4 array and iterate over it."""

import numpy as np

if __name__ == "__main__":
    # arr = np.random.random((3,4))
    # OR
    arr = np.arange(10,22).reshape((3,4))
    print("Array: ",arr)
    print("Elements of 3x4 generated array: ")
    for i in np.nditer(arr):
        print(i,end=" ")
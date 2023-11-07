#!/usr/bin/python3

"""Write a NumPy program to create a 4x4 array with 
random values. Create an array from the said array swapping first and last rows."""

import numpy as np

if __name__ == "__main__":
    np.random.seed(10)
    arr = np.random.random((4,4))
    print("Original array: \n",arr)
    arr[[0,-1],:] = arr[[-1,0],:]
    print("Array after swapping: \n",arr)
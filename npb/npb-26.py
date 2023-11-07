#!/usr/bin/python3

"""Write a NumPy program to find the number of rows and columns in a given matrix."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([[10,11,12,13],[14,15,16,17],[18,19,20,21]])

    print("Given Array: \n",arr)
    print("\nNumber of rows and columns: ",arr.shape)
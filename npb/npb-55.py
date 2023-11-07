#!/usr/bin/python3

"""Write a NumPy program to create an zeros array of equal shape and data type for a given array."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([[5.54, 3.38, 7.99], [3.54, 8.32, 6.99], [1.54, 2.39, 9.29]])
    print("Original array:\n",arr)
    print("Zeroes array similar to above array:\n",np.zeros_like(arr))
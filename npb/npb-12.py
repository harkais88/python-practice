#!/usr/bin/python3

"""Write a NumPy program to create an array with the values 1, 7, 13, 105 and 
determine the size of the memory occupied by the array."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([1, 7, 13, 105])
    print("Original array: ",arr)
    print("Memory Occupied by array: ",arr.size * arr.itemsize," bytes")
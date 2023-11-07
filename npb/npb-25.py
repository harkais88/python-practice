#!/usr/bin/python3

"""Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21."""

import numpy as np

if __name__ == "__main__":
    arr = np.arange(10,22).reshape((3,4))
    print("3x4 matrix filled with values from 10 to 21:")
    print(arr)
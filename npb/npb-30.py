#!/usr/bin/python3

"""Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal."""

import numpy as np

if __name__ == "__main__":
    matrix = np.zeros((4,4))
    matrix[::2,1::2] = 1
    matrix[1::2,::2] = 1

    print("4x4 matrix with 0s and 1s staggered, with main diagonal as 0s: \n",matrix)
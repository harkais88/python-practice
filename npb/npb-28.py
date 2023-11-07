#!/usr/bin/python3

"""Write a NumPy program to create a 10x10 matrix, in which the 
elements on the borders will be equal to 1, and inside 0."""

import numpy as np

if __name__ == "__main__":
    matrix = np.ones((10,10))
    matrix[1:-1,1:-1] = 0
    print("10x10 matrix with 1s around border and 0s inside: \n")
    print(matrix)
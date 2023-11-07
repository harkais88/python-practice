#!/usr/bin/python3

"""Write a NumPy program to create a 3x3 identity matrix."""

import numpy as np

if __name__ == "__main__":
    matrix = np.identity(3)
    print("3x3 Identity matrix: \n",matrix)
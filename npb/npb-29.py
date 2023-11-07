#!/usr/bin/python3

"""Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5."""

import numpy as np

if __name__ == "__main__":
    arr = np.diag([1,2,3,4,5])
    print("5x5 zero matrix with elements on the main diagonal equal to 1,2,3,4,5: \n",arr)
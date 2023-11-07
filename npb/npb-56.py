#!/usr/bin/python3

"""Write a NumPy program to create a three-dimensional array with the shape (3,5,4) and set it to a variable."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.randint(0,10,(3,5,4))
    print(arr)
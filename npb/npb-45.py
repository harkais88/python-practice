#!/usr/bin/python3

"""Write a NumPy program to create a one-dimensional array of single, two and three-digit numbers."""

import numpy as np

if __name__ == "__main__":
    print("1-D Array of single digit numbers:\n",np.arange(0,10))
    print("1-D Array of two digit numbers:\n",np.arange(10,21))
    print("1-D Array of three digit numbers:",np.arange(100,201))
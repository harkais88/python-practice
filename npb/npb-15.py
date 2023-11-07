#!/usr/bin/python3

"""Write a NumPy program to create an array of all even integers from 30 to 70."""

import numpy as np

if __name__ == "__main__":
    arr = np.arange(30,71,2)
    print("Array of even integers from 30 to 70: ",arr)
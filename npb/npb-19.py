#!/usr/bin/python3

"""Write a NumPy program to create a vector with values ranging 
from 15 to 55 and print all values except the first and last."""

# Vector is basically just a one-dimensional array, so....

import numpy as np

if __name__ == "__main__":
    arr = np.arange(15,56)
    print("Vector ranging from 15 to 55 excluding the first and last: ",arr[1:-1])
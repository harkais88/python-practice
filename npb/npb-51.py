#!/usr/bin/python3

"""Write a NumPy program to create a new array of given shape (5,6) and type, filled with zeros intially."""

import numpy as np

if __name__ == "__main__":
    arr = np.zeros((5,6))
    print("Zeros array of shape 5x6: ",arr)
    arr[::2,::2] = 3
    arr[1::2,::2] = 7
    print("Partially filled array: ",arr)
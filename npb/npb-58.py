#!/usr/bin/python3

"""Write a NumPy program to swap rows and columns of a given array in reverse order."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.randint(1,10,(4,4))
    print("Original array:\n",arr)
    arr = arr[::-1,::-1]
    print("Reversed array:\n",arr)
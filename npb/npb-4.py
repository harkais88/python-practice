#!/usr/bin/python3

"""Write a NumPy program to test if any of the elements of a given array are non-zero. """

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([0,0,0,0])
    arr2 = np.array([0,1,0,0])

    print(f"Are any of the elements of array {arr1} non-zero? ",arr1.any())
    print(f"Are any of the elements of array {arr2} non-zero? ",arr2.any())

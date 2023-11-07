#!/usr/bin/python3

"""Write a NumPy program to check whether two arrays with precision are equal (element wise) or not."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([0.5, 1.5, 0.2])
    arr2 = np.array([0.4999999999, 1.500000000, 0.2])
    np.set_printoptions(precision=15)
    print("Checking the arrays are equal element wise: ",np.equal(arr1,arr2))
    arr3 = np.array([0.5, 1.5, 0.23])
    arr4 = np.array([0.4999999999, 1.5000000001, 0.23])
    np.set_printoptions(precision=15)
    print("Checking the arrays are equal element wise: ",arr3==arr4)
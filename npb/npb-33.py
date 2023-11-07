#!/usr/bin/python3

"""Write a NumPy program to compute the inner product of two given vectors."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([5,6,7,8])
    print(f"Inner Product of {arr1} and {arr2}: {np.dot(arr1,arr2)}")
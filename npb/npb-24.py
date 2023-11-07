#!/usr/bin/python3

"""Write a NumPy program to multiply the values of two given vectors."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([5,6,7,8])

    print(f"Multiplying {arr1} and {arr2}: ",arr1 * arr2)
    #OR
    # print(f"Multiplying {arr1} and {arr2}: ",np.multiply(arr1,arr2))
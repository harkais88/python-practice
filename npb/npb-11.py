#!/usr/bin/python3

"""Write a NumPy program to create an element-wise comparison 
(equal, equal within a tolerance) of two given arrays."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
    arr2 = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

    print(f"Are {arr1} and {arr2} equal? {np.equal(arr1,arr2)}")
    print(f"Are {arr1} and {arr2} equal within a tolerance? {np.allclose(arr1,arr2)}")

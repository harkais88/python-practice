#!/usr/bin/python3

"""Write a NumPy program to create an element-wise comparison 
(greater, greater_equal, less and less_equal) of two given arrays."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.random.random(4)
    arr2 = np.random.random(4)

    print(f"Comparing arrays {arr1} and {arr2} element wise for ")
    print(f"greater: {np.greater(arr1,arr2)}")
    print(f"greater and equal: {np.greater_equal(arr1,arr2)}")
    print(f"lesser: {np.less(arr1,arr2)}")
    print(f"lesser and equal: {np.less_equal(arr1,arr2)}")
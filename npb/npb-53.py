#!/usr/bin/python3

"""Write a NumPy program to extract all numbers from a given array less and greater than a specified number."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([[5.54, 3.38, 7.99], [3.54, 4.38, 6.99], [1.54, 2.39, 9.29]])
    print("Original array: \n",arr)
    print("Array elements greater than 5: \n",arr[arr>5])
    print("Array elements lesser than 6: \n",arr[arr<6])
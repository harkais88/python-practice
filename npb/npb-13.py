#!/usr/bin/python3

"""Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives. """

import numpy as np

if __name__ == "__main__":
    arr0 = np.zeros(10)
    print("Array of 10 zeroes: ",arr0)
    arr1 = np.ones(10)
    print("Array of 10 ones: ",arr1)
    # arr5 = np.repeat(5,10)
    #OR
    arr5 = np.ones(10) * 5
    print("Array of 10 fives: ",arr5)
#!/usr/bin/python3

"""Write a NumPy program to test whether none of the elements of a given array are zero. """

import numpy as np

if __name__ == "__main__":
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([0,1,2,3])

    print(f"Are all elements of {arr1} non-zero? {arr1.all()}")
    print(f"Are all elements of {arr2} non-zero? {arr2.all()}")
    
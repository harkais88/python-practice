#!/usr/bin/python3

"""Write a NumPy program to find missing data in a given array."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([1,2,3,np.nan,4,np.nan,5])
    print("Missing data in ",arr,": ",np.isnan(arr))
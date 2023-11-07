#!/usr/bin/python3

"""Write a NumPy program to test element-wise for NaN of a given array."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([0,1,np.NINF,np.nan,np.inf])

    print(f"Checking array {arr} element-wise for NaN of a given array: ",np.isnan(arr))
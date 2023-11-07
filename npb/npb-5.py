#!/usr/bin/python3

"""Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number)."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([0,1,np.nan,np.Inf])

    print(f"Checking array {arr} element wise for finiteness: ",np.isfinite(arr))
    
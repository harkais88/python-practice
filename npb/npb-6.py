#!/usr/bin/python3

"""Write a NumPy program to test elements-wise for positive or negative infinity. """

import numpy as np

if __name__ == "__main__":
    arr = np.array([0,1,np.NINF,np.Inf,np.nan])
    
    print(f"Checking array {arr} elementwise for positive or negative infinity: {np.isinf(arr)}")
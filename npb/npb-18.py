#!/usr/bin/python3

"""Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution."""

import numpy as np

if __name__ == "__main__":
    #arr = np.random.randn(15)
    #OR
    arr = np.random.normal(0,1,size = 15)
    print("Array of 15 random numbers from a standard normal distribution: \n",arr)
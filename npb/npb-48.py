#!/usr/bin/python3

"""Write a NumPy program to create a two-dimensional 
array with shape (8,5) of random numbers. Select random numbers from a normal distribution (200,7)."""

import numpy as np

if __name__ == "__main__":
    # arr = np.random.randint(7,200,(8,5))
    # print("2-D array with shape (8,5) of random numbers from normal distribution (200,7):\n",arr)

    #Given in the site
    np.random.seed(20) 
    cbrt = np.cbrt(7)
    nd1 = 200 
    print(cbrt * np.random.randn(10, 4) + nd1)
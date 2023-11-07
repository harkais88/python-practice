#!/usr/bin/python3

"""Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50."""

import numpy as np

if __name__ == "__main__":
    arr = np.linspace(5,50,10)
    print("Vector of length 10 with values evenly distributed between 5 and 50: ",arr)
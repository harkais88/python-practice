#!/usr/bin/python3

"""Write a NumPy program to create a vector with values from 0 to 20 
and change the sign of the numbers in the range from 9 to 15."""

import numpy as np

if __name__ == "__main__":
    arr = np.arange(0,21)
    arr[(arr >= 9) & (arr <= 15)] *= -1
    print("Resultant Vector: ",arr)
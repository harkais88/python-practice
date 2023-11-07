#!/usr/bin/python3

"""Write a NumPy program to compute the sum of all elements, 
the sum of each column and the sum of each row in a given array."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.randint(1,10,(4,4))
    print("Given Array:\n",arr)
    print("Sum of all elements: ",np.sum(arr))
    print("Sum of each column: ",np.sum(arr,axis=0))
    print("Sum of each row: ",np.sum(arr,axis=1))
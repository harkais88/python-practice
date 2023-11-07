#!/usr/bin/python3

"""Write a NumPy program to create a 4x4 array. 
Create an array from said array by swapping first and last, second and third columns."""

import numpy as np

if __name__ == "__main__":
    arr = np.random.randint(1,10,(4,4))
    print("Original Array:\n",arr)
    arr[:,[0,-1]] = arr[:,[-1,0]]
    arr[:,[1,-2]] = arr[:,[-2,1]]
    print("Array after swapping first column with last column, and second column with third column:")
    print(arr)
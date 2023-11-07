#!/usr/bin/python3

"""Write a NumPy program to create a two-dimensional array of a specified format."""

import numpy as np

if __name__ == "__main__":
    #The following 2-d arrays are the same
    print("2-D Array:\n",np.arange(1,151).reshape((15,10)))

    #-1 is given when we don't want to specify a format
    #This works because we also mention the array to have 10 columns, and for this
    #sample (1-150), we can do that evenly with 15 rows
    print("2-D Array:\n",np.arange(1,151).reshape((-1,10)))

    #So similarily... 
    print("2-D Array:\n",np.arange(1,151).reshape((15,-1)))
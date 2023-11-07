#!/usr/bin/python3

"""Write a NumPy program to save a given array to a text file and load it."""

import numpy as np

if __name__ == "__main__":
    #Don't forget to delete the temporary file created after this
    arr = np.arange(10,22).reshape((4,3))
    np.savetxt("temp.txt",arr,fmt="%d",header="col1 col2 col3")
    print("Loading data from temp.txt")
    print(np.loadtxt("temp.txt"))
#!/usr/bin/python3

"""Write a NumPy program to save a given array to a binary file ."""

import numpy as np
from tempfile import TemporaryFile #For using a temporary file
from os.path import exists

if __name__ == "__main__":
    outfile = TemporaryFile()
    arr = np.linspace(10,100,10)
    np.save(outfile,arr)
    _ = outfile.seek(0) #Only needed here to simulate closing and reopening file
    print("Checking if the file exists? ")
    if exists(outfile.name):
        print("Yeah, checking whether the saved array is equal to our array ",arr,":",end="")
        print(np.array_equal(np.load(outfile),arr))

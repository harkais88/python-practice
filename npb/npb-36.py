#!/usr/bin/python3

"""Write a NumPy program to save two given arrays into a single 
file in compressed format (.npz format) and load it."""

import numpy as np
from tempfile import TemporaryFile #For using a temporary file
from os.path import exists

if __name__ == "__main__":
    x = np.arange(10)
    y = np.sin(x)

    outfile = TemporaryFile()
    np.savez(outfile, x=x, y=y)
    _ = outfile.seek(0) #Only needed here to simulate the closing and reopening of file
    if exists(outfile.name):
        print("Zip Successfully Created")
        arrs = np.load(outfile)
        print("File Names Created: ",arrs.files)
        print("Loaded arrays are: ")
        print("x : ",arrs['x'])
        print("y : ",arrs['y'])

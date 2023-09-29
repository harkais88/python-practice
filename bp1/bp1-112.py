#!/usr/bin/python3

"""Write a Python program to make file lists from the current directory using a wildcard. """

import os
import glob

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))

    print("\n Filenames starting with bp1-10: ", glob.glob(os.path.basename(os.path.join(path, "bp1-10*"))))
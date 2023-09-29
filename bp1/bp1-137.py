#!/usr/bin/python3

"""Write a Python program to find files and skip directories in a given directory. """

import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print("\nFiles under {}: {}\n".format(path, ", ".join([file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))])))

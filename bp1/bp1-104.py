#!/usr/bin/python3

"""Write a Python program to extract the filename from a given path."""

import os

if __name__ == "__main__":
    print(os.path.basename(__file__))
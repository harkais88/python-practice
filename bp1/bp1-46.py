#!/usr/bin/python3

"""Write a Python program to retrieve the path and name of the file currently being executed."""

import os

if __name__ == "__main__":
    print("\n ",os.path.realpath(__file__))
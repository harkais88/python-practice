#!/usr/bin/python3

"""Write a Python program to get the size of a file."""

import os

if __name__ == "__main__":
    file_path = os.path.abspath(__file__)
    print("\n Size of {}: {} bytes".format(file_path,os.path.getsize(file_path)))
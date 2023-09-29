#!/usr/bin/python3

"""Write a Python program to divide a path by the extension separator. """

import os

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)

    print("Dividing up path ",script_path,": ", os.path.splitext(script_path))
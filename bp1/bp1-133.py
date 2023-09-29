#!/usr/bin/python3

"""Write a Python program to list the home directory without an absolute path. """

import os

if __name__ == "__main__":
    print("Listing the home directory {}: {}".format(os.path.expanduser("~"), os.listdir(os.path.expanduser("~"))))
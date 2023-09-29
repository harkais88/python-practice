#!/usr/bin/python3

"""Write a Python program to test whether the system is a big-endian platform or a little-endian platform."""

import sys

if __name__ == "__main__":
    if sys.byteorder == "little":
        print("The System is a Little-Endian Platform")
    else:
        print("The System is a Big-Endian Platform")
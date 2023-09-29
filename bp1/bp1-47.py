#!/usr/bin/python3

"""Write a Python program to find out the number of CPUs used."""

import os

if __name__ == "__main__":
    print("\n Number of CPUs used: ",os.cpu_count())

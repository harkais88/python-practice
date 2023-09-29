#!/usr/bin/python3

"""Write a Python program to access environment variables."""

import os

if __name__ == "__main__":
    print(type(os.environ))
    print("----------------------------------------")
    print(os.environ["PATH"]) #Accessing a particular ENV variable
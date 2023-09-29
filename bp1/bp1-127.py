#!/usr/bin/python3

"""Write a Python program to get the actual module object for a given object. """

from inspect import getmodule
from math import sqrt

def add(x,y):
    return x+y

if __name__ == "__main__":
    print(getmodule(type))
    print(getmodule(sqrt))
    print(getmodule(add))
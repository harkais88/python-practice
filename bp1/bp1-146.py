#!/usr/bin/python3

""" Write a Python program to find the location of Python module sources. """

import imp
import inspect
import os
import math

if __name__ == "__main__":
    # You can either use the depreceated find_module function under the imp module
    print("Location of os module: {}".format(imp.find_module('os')))    
    print("List of directories in os module: ",os.path)

    # Or you could use the inspect module's getfile and getsourcefile methods
    try:
        print("os module location: ",inspect.getfile(os))
        print("os module location: ",inspect.getsourcefile(os))
        print("math module location: ",inspect.getfile(math)) # Does not work for built-in modules, it will raise a TypeError
    except TypeError:
        print("math module location can't be found this way, as it is a built-in module")
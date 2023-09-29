#!/usr/bin/python3

"""Write a Python program to get the Identity, Type, and Value of an object."""

if __name__ == "__main__":
    #Let our object be the following
    x = 2

    print("\n Identity of x: {}".format(id(x)))
    print("\n Type of x: {}".format(type(x)))
    print("\n Value of x: {}".format(x))
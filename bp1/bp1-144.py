#!/usr/bin/python3

""" Write a Python program to check whether a variable is an integer or string. """

def chckType(var):
    if isinstance(var,int):
        print(var, "is an integer")
    else:
        print(var, "is not an integer")

    if isinstance(var,str):
        print(var, "is a string")
    else:
        print(var, "is not a string")

    if not (isinstance(var,int) or isinstance(var,str)):
        print(var, "is nor a string or an integer")

if __name__ == "__main__":
    var1 = 12
    var2 = "12"
    var3 = [12]

    chckType(var1)
    chckType(var2)
    chckType(var3)

#!/usr/bin/python3

"""Write a Python program to test if a variable is a list, tuple, or set. """

def chckType(var):
    if isinstance(var,list):
        print(var, "is a list")
    elif isinstance(var,tuple):
        print(var, "is a tuple")
    elif isinstance(var,set):
        print(var, "is a set")
    else:
        print(var, "is neither a list, tuple or set")

if __name__ == "__main__":
    var1 = [12,13]
    var2 = (12,13)
    var3 = {12,13}
    var4 = (12)

    chckType(var1)
    chckType(var2)
    chckType(var3)
    chckType(var4) # Interesting observation
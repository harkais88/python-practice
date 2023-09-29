#!/usr/bin/python3

"""Write a Python program to determine if a variable is defined or not. """

if __name__ == "__main__":
    var1 = 1

    try:
        print(var1, "exists")
        print(var2, "exists")
    except NameError:
        print("Variable not defined")
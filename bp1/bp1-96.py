#!/usr/bin/python3

"""Write a Python program to check whether a string is numeric."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")

    if string.isnumeric():
        print("\n It is a numeric string")
    else:
        print("\n It is not a numeric string")
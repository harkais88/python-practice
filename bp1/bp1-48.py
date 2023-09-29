#!/usr/bin/python3

"""Write a Python program to parse a string to float or integer."""

if __name__ == "__main__":
    string = input("\n Enter a number: ")

    print(string,type(string))
    string = float(string)
    print(string,type(string))
    string = int(string)
    print(string,type(string))
#!/usr/bin/python3

"""Write a Python program to remove the first and last elements from a given string.
Original string: PHP
Removing the first and last elements from the said string: H
Original string: Python
Removing the first and last elements from the said string: ytho
Original string: JavaScript
Removing the first and last elements from the said string: avaScrip"""

def rmvFirstAndLastChars(string):
    print("Original string: ",string)
    print("Removing the first and last elements from the said string: ",end="")
    print(string if len(string) < 3 else string[1:len(string)-1])

if __name__ == "__main__":
    rmvFirstAndLastChars("PHP")
    rmvFirstAndLastChars("Python")
    rmvFirstAndLastChars("Javascript")
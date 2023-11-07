#!/usr/bin/python3

"""Write a Python program to find the central character(s) of a given string. 
Return the two middle characters if the length of the string is even. 
Return the middle character if the length of the string is odd.
Original string: Python
Middle character(s) of the said string: th
Original string: PHP
Middle character(s) of the said string: H
Original string: Java
Middle character(s) of the said string: av"""

def getCenterChar(string):
    print("Original string: ",string)
    print("Middle character(s) of the said string: ",end="")
    print(string[len(string)//2] if len(string) % 2 != 0 else string[len(string)//2 - 1]+string[len(string)//2])

if __name__ == "__main__":
    getCenterChar("Python")
    getCenterChar("PHP")
    getCenterChar("Java")
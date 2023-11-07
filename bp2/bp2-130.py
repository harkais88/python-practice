#!/usr/bin/python3

"""Write a Python program to get the index number of all lower case letters in a given string.
Original string: Python
Indices of all lower case letters of the said string: [1, 2, 3, 4, 5] Original string: JavaScript
Indices of all lower case letters of the said string: [1, 2, 3, 5, 6, 7, 8, 9] Original string: PHP
Indices of all lower case letters of the said string: []"""

def getLowerIndices(string):
    print("Original string: ",string)
    print("Indices of all lower case letters of the said string: ",
    #       [i for i,char in enumerate(string) if char.islower()])

    # OR
            [i for i in range(len(string)) if string[i].islower()])
    

if __name__ == "__main__":
    getLowerIndices("Python")
    getLowerIndices("JavaScript")
    getLowerIndices("PHP")

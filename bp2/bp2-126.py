#!/usr/bin/python3

"""Write a Python program to reverse a given string in lower case.
Original string: PHP
Reverse the said string in lower case: php
Original string: JavaScript
Reverse the said string in lower case: tpircsavaj
Original string: PHPP
Reverse the said string in lower case: pphp"""

def revStringInLower(string):
    print("Original string: ",string)
    print("Reverse the said string in lower case: ",string[::-1].lower())

if __name__ == "__main__":
    revStringInLower("PHP")
    revStringInLower("JavaScript")
    revStringInLower("PHPP")
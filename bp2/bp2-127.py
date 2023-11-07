#!/usr/bin/python3

"""Write a Python program to convert the letters of a given string (same case-upper/lower) into alphabetical order.
Original string: PHP
Convert the letters of the said string into alphabetical order: HPP
Original string: javascript
Convert the letters of the said string into alphabetical order: aacijprstv
Original string: python
Convert the letters of the said string into alphabetical order: hnopty"""

def sortChars(string):
    print("Original string: ",string)
    print("Convert the letters of the said string into alphabetical order: ")
    # print("".join([chr(i) for i in sorted([ord(j) for j in list(string)])]))
    # OR
    print("".join(sorted(string)))

if __name__ == "__main__":
    sortChars("PHP")
    sortChars("javascript")
    sortChars("python")
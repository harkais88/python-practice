#!/usr/bin/python3

"""Write a Python program to remove all vowels from a given string.
Original string: Python
After removing all the vowels from the said string: Pythn
Original string: C Sharp
After removing all the vowels from the said string: C Shrp
Original string: JavaScript
After removing all the vowels from the said string: JvScrpt"""

def rmvVowels(string):
    print("Original string: ",string)
    print("After removing all the vowels from the said string: ",end = "")
    print("".join([i for i in string if i.lower() not in ["a","e","i","o","u"]]))

if __name__ == "__main__":
    rmvVowels("Python")
    rmvVowels("C Sharp")
    rmvVowels("JavaScript")
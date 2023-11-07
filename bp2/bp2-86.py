#!/usr/bin/python3

"""From Wikipedia:
An isogram (also known as a "nonpattern word") is a logological term for a 
word or phrase without a repeating letter. It is also used by some people 
to mean a word or phrase in which each letter appears the same number of 
times, not necessarily just once. Conveniently, the word itself is an isogram 
in both senses of the word, making it autological.
Write a Python program to check whether a given string is an "isogram" or not.
Sample Input:
("w3resource")
("w3r")
("Python")
("Java")
Sample Output:
False
True
True
False"""

def isIsogram(string):
    return len(set(string.lower())) == len(string)

if __name__ == "__main__":
    print(isIsogram("w3resource"))
    print(isIsogram("w3r"))
    print(isIsogram("Python"))
    print(isIsogram("Java"))

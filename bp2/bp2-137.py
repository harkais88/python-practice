#!/usr/bin/python3

""" Write a Python program to reverse all words of odd lengths.
Original string: The quick brown fox jumps over the lazy dog
Reverse all the words of the said string which have odd length: ehT kciuq nworb xof spmuj over eht lazy god
Original string: Python Exercises
Reverse all the words of the said string which have odd length: Python sesicrexE"""

def revOdds(string):
    print("Original string: ",string)
    print("Reverse all the words of the said string which have odd length: ",end="")
    print(" ".join([i if len(i) % 2 == 0 else i[::-1] for i in string.split()]))

if __name__ == "__main__":
    revOdds("The quick brown fox jumps over the lazy dog")
    revOdds("Python Exercises")
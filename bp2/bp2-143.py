#!/usr/bin/python3

"""Write a Python program to check if every consecutive sequence of zeroes is followed 
by a consecutive sequence of ones of the same length in a given string. Return True/False.
Original sequence: 001011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 0011101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False"""

import re

def checkConsecutiveZeroesandOnes(num:str):
    print("Original sequence: ",num)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print([len(i) for i in re.findall("0+",num)] == [len(i) for i in re.findall("1+",num)])

if __name__ == "__main__":
    checkConsecutiveZeroesandOnes("001011")
    checkConsecutiveZeroesandOnes("01010101")
    checkConsecutiveZeroesandOnes("00")
    checkConsecutiveZeroesandOnes("000111000111")
    checkConsecutiveZeroesandOnes("00011100011")
    checkConsecutiveZeroesandOnes("0011101")
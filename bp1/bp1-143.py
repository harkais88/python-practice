#!/usr/bin/python3

"""Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
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
False"""

def seq(str):
    print("Original sequence: ",str, "\nCheck if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")

    while "01" in str:
        str = str.replace("01","")

    print(len(str) == 0)

if __name__ == "__main__":
    seq("01010101")
    seq("00")
    seq("000111000111")
    seq("00011100011")
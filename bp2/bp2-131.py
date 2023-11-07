#!/usr/bin/python3

"""Write a Python program to count the number of zeros and ones in the binary representation of a given integer.
Original number: 12
Number of ones and zeros in the binary representation of the said number: Number of zeros: 2, Number of ones: 2
Original number: 1234
Number of ones and zeros in the binary representation of the said number: Number of zeros: 6, Number of ones: 5"""

def zeroOneInBinCount(num):
    print("Original number: ",num)
    print("Number of ones and zeros in the binary representation of the said number: ",end = "")
    b_num = str(bin(num)).replace("0b","")
    print(f"Number of zeros: {b_num.count('0')}, Number of ones: {b_num.count('1')}")

if __name__ == "__main__":
    zeroOneInBinCount(12)
    zeroOneInBinCount(1234)
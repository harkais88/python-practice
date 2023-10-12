#!/usr/bin/python3

"""Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
Range of the number(n): (1 <= n <= 2*109)."""

from math import factorial

def getZeroCount(num):
    count = 0
    num = str(num)
    for i in range(len(num) - 1,0,-1):
        if num[i] == "0":
            count += 1
        else:
            break
    return count

def getFactEndZeros(num):
    print(f" Number of zeroes at the end of {num}!: {getZeroCount(factorial(num))}")

if __name__ == "__main__":
    # getFactEndZeros(5)
    # getFactEndZeros(2*109)

    for i in range(1,(2*109) + 1):
        getFactEndZeros(i)
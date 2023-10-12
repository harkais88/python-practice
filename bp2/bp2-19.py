#!/usr/bin/python3

"""Write a Python program that finds the value of n when n degrees of number 2 are written 
sequentially on a line without spaces between them."""

# Considering num would always be a perfect 2^n number
# def getN(num):
#     n = -1
#     while num != 0:
#         if num % 2 != 0:
#             return "non-whole number"
#         num = num // 2
#         n += 1
#     return n

# Considering num is not a perfect 2^n number
from math import log2

def getN(num):
    return log2(num)

if __name__ == "__main__":
    num = int(input("\n Enter a number: "))

    print(" 2 to the power of {:.4} = {}".format(getN(num),num))
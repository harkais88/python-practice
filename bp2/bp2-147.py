#!/usr/bin/python3

"""A Python list contains two positive integers. 
Write a Python program to check whether the cube root of 
the first number is equal to the square root of the second number.
Sample Data:
([8, 4]) -> True
([64, 16]) -> True
([64, 36]) -> False"""

from math import cbrt,sqrt

def cbrtEqualsqrt(nums):
    print(f"({nums}) -> {cbrt(nums[0]) == sqrt(nums[1])}")

if __name__ == "__main__":
    cbrtEqualsqrt([8, 4])
    cbrtEqualsqrt([64, 16])
    cbrtEqualsqrt([64, 36])
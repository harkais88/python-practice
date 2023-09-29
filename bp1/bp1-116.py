#!/usr/bin/python3

"""Write a Python program to compute the product of a list of integers (without using a for loop)"""

from random import randint

if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(10)]

    print("Number list: ",nums)

    # One way to do it
    # from functools import reduce
    # print("Product of all numbers in list: ",reduce(lambda x,y: x*y, nums))

    # Another way to do it
    from math import prod
    print("Product of all numbers in list: ",prod(nums))
#!/usr/bin/python3

"""Write a Python program that removes and prints every third number 
from a list of numbers until the list is empty."""

from random import randint

if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(12)] #randint(11,101)

    print(f" Printing every third number from the list {nums}: ",end = "")

    result = []
    while len(nums) != 0:
        if len(nums) > 2:
            index = 2
        else:
            index = len(nums) - 1
        while index < len(nums):
            result.append(nums.pop(index))
            index += 2

    print(", ".join([str(ele) for ele in result]))
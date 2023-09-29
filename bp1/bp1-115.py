#!/usr/bin/python3

"""Write a Python program to filter positive numbers from a list. """

from random import randint

if __name__ == "__main__":
    nums = [randint(-100,100) for _ in range(10)]

    print("Generated List: ",nums)
    print("Positive numbers from this list: ", list(ele for ele in nums if ele > 0))
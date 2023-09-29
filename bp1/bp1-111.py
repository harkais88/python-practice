#!/usr/bin/python3

"""Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. """

from random import randint

if __name__ == "__main__":
    nums = [randint(15,150) for _ in range(10)]

    print("\n Numbers divisible by 15: ", list(filter(lambda ele: (ele % 15 == 0), nums)))
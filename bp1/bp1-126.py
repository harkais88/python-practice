#!/usr/bin/python3

"""Write a Python program to sum all counts in a collection."""

from random import randint
from collections import Counter

if __name__ == "__main__":
    nums = [randint(0,9) for _ in range(100)]

    count = Counter(nums)

    print("Sum of all counts in a collection: ",sum(count.values()))
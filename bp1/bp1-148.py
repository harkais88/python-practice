#!/usr/bin/python3

"""Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions."""

from random import randint

def max(list):
    max = list[0]
    for i in range(1,len(list)):
        if list[i] > max:
            max = list[i]
    return max

def min(list):
    max = list[0]
    for i in range(1,len(list)):
        if list[i] < max:
            max = list[i]
    return max

if __name__ == "__main__":
    list = [randint(-100,100) for _ in range(100)]

    print(" Generated List: ",list)
    print("\n Max from list: {}\n Min from list: {}".format(max(list),min(list)))
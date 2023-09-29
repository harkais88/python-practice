#!/usr/bin/python3

"""Write a Python program to check if a number is positive, negative or zero. """

from random import randint

if __name__ == "__main__":
    list = [randint(-10,10) for _ in range(10)]

    for num in list:
        if num == 0:
            print(num, " is zero")
        elif num < 0:
            print(num, " is negative")
        else:
            print(num, " is positive")
#!/usr/bin/python3

""" Write a Python program that uses double quotes to display strings.
Hint: Use the dumps function from the json module """

from json import dumps

if __name__ == "__main__":
    print(dumps({'A': 1, 'B': 2}))
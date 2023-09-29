#!/usr/bin/python3

"""Write a Python program to extract a single key-value pair from a dictionary into variables. """

if __name__ == "__main__":
    dict = {"A": 1, "B": 2, "C": 3}

    x,y = list(dict.items())[1]

    print(x,y)
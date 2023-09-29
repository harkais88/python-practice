#!/usr/bin/python3

"""Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)"""

def sums(obj):
    print("\n Sum of {}: {}".format(obj,sum(obj)))

if __name__ == "__main__":
    list = [1,2,3,4]
    tuple = (1,2,3,4)
    set = {1,2,3,4}
    dict = {"A": 1, "B": 2, "C": 3, "D": 4}

    sums(list)
    sums(tuple)
    sums(set)
    sums(dict.values())
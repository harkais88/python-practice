#!/usr/bin/python3

"""Write a Python program to split a variable length string into variables. """

if __name__ == "__main__":
    nums = ["a", "b", 100]

    # We could simply do it by this
    a,b,c = nums
    print(a,b,c)

    # Or we could do this instead.... for no reason at all
    a,b,c = (nums + [None] * 3)[:3]
    print(a,b,c)
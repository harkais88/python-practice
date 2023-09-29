#!/usr/bin/python3

"""Write a Python program to create a bytearray from a list. """

from random import randint

if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(10)]

    print("\n Original List: ",nums)

    # bytearray returns a mutable array of bytes of the given size and initialization values
    nums = bytearray(nums)

    # Could be useful when getting the bytearray of a string consisting of unicode code points
    str = u"\u0041\u0072\u006B\u0061"
    print(" My name: ",bytearray(str, "utf-8"))

    print("\n Bytearray of above List: ",nums)

    print("\n Printing each element of Bytearray")
    for i in nums:
        print(" ",i,end = "")
    print()
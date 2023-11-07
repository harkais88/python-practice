#!/usr/bin/python3

"""Write a Python program that takes a positive integer and 
calculates the cube root of the number until the number is less than three. 
Count the number of steps to complete the task.
Sample Data:
(3) -> 1
(39) -> 2
(10000) -> 2"""

from math import cbrt

def countNoOfCubeRoots(num):
    print(f"({num}) -> ",end = "")
    count = 0
    while num >= 3:
        num = cbrt(num)
        count += 1
    print(count)

if __name__ == "__main__":
    countNoOfCubeRoots(3)
    countNoOfCubeRoots(39)
    countNoOfCubeRoots(10000)
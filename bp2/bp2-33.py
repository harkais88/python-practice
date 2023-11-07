#!/usr/bin/python3

"""Write a Python program to find the heights of the top three buildings in descending order 
from eight given buildings.
Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25,35,15,16,30,45,37,39
Heights of the top three buildings:
45,39,37"""

def getTop3Height(list):
    list = sorted(list)
    list.reverse()
    return list[0:3]

if __name__ == "__main__":
    print(getTop3Height([25,35,15,16,30,45,37,39]))
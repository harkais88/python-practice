#!/usr/bin/python3

"""Write a Python program to check whether a sequence of numbers has an increasing trend or not.
Sample Input:
[1,2,3,4]
[1,2,5,3,4]
[-1,-2,-3,-4]
[-4,-3,-2,-1]
[1,2,3,4,0]
Sample Output:
True
False
False
True
False"""

def checkIncreaseTrend(list):
    return sorted(list) == list

if __name__ == "__main__":
    print(checkIncreaseTrend([1,2,3,4]))
    print(checkIncreaseTrend([1,2,5,3,4]))
    print(checkIncreaseTrend([-1,-2,-3,-4]))
    print(checkIncreaseTrend([-4,-3,-2,-1]))
    print(checkIncreaseTrend([1,2,3,4,0]))
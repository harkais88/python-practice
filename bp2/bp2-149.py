#!/usr/bin/python3

""" Python list contains some positive integers. 
Write a Python program to count the numbers that are greater than the previous number on the list.
Sample Data:
([1, 4, 7, 9, 11, 5]) -> 4
([1, 3, 3, 2, 2]) -> 1
([4, 3, 2, 1]) -> 0"""

def noOfNosGreaterThanPrev(nums):
    print(f"({nums}) -> ",end = "")
    print([nums[i] > nums[i-1] for i in range(1,len(nums))].count(True))

if __name__ == "__main__":
    noOfNosGreaterThanPrev([1, 4, 7, 9, 11, 5])
    noOfNosGreaterThanPrev([1, 3, 3, 2, 2])
    noOfNosGreaterThanPrev([4, 3, 2, 1])
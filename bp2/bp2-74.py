#!/usr/bin/python3

"""Write a Python program that removes duplicate elements 
from a given array of numbers so that each element appears only once and returns the new length of the array.
Sample Input:
[0,0,1,1,2,2,3,3,4,4,4]
[1, 2, 2, 3, 4, 4]
Sample Output:
5
4"""

def lengthAfterDupRemove(li):
    return len(set(li))

if __name__ == "__main__":
    print(lengthAfterDupRemove([0,0,1,1,2,2,3,3,4,4,4]))
    print(lengthAfterDupRemove([1, 2, 2, 3, 4, 4]))
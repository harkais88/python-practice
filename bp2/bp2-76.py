#!/usr/bin/python3

"""Write a Python program to remove all instances of a given value 
from a given array of integers and find the length of the newly created array.
Sample Input:
([1, 2, 3, 4, 5, 6, 7, 5], 5)
([10,10,10,10,10], 10)
([10,10,10,10,10], 20)
([], 1)
Sample Output:
6
0
5
0"""

def lenAfterRemoval(list,key):
    return len([ele for ele in list if ele != key])

if __name__ == "__main__":
    print(lenAfterRemoval([1, 2, 3, 4, 5, 6, 7, 5], 5))
    print(lenAfterRemoval([10,10,10,10,10], 10))
    print(lenAfterRemoval([10,10,10,10,10], 20))
    print(lenAfterRemoval([], 1))
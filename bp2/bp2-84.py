#!/usr/bin/python3

"""Write a Python program to test whether a given number is symmetrical or not.
A number is symmetrical when it is equal to its reverse.
Sample Input:
(121)
(0)
(122)
(990099)
Sample Output:
True
True
False
True"""

def isSymmetrical(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(isSymmetrical(121))
    print(isSymmetrical(0))
    print(isSymmetrical(122))
    print(isSymmetrical(990099))
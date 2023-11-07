#!/usr/bin/python3

"""Write a Python program to identify non-prime numbers between 1 and 100 (integers). Print the non-prime numbers.
Sample Input:
range(1, 101)
Sample Output:
Nonprime numbers between 1 to 100:
4
6
8
9
10
..
96
98
99
100"""

from math import sqrt

def isNotPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return True
    return False

if __name__ == "__main__":
    for i in filter(isNotPrime, range(1,101)): print(i);
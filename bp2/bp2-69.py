#!/usr/bin/python3

"""Write a Python program that counts the number of prime numbers that are less than a given non-negative number.
Sample Input:
(10)
(100)
Sample Output:
4
25"""

from math import sqrt

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0 and num != i:
            return False
    return True

def getPrimeCounts(n):
    count = 0
    for i in range(2,n+1):
        if isPrime(i):
            count += 1

    return count

if __name__ == "__main__":
    print(getPrimeCounts(10))
    print(getPrimeCounts(100))
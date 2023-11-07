#!/usr/bin/python3

"""Write a Python program to compute the sum of the first n prime numbers.
Input:
Input a number (n<=10000) to compute the sum:
25
Sum of first 25 prime numbers:
1060"""

from math import sqrt

def isPrime(n):
    for i in range(2,int(sqrt(n)+1)):
        if (n%i == 0):
            return False
    return True

if __name__ == "__main__":
    n = int(input("Input a number (n<=10000) to compute the sum:\n"))
    primes = []
    i = 2
    while len(primes) < 25:
        if isPrime(i):
            primes.append(i)
        i += 1
    print(f"Sum of first {len(primes)} prime numbers:\n{sum(primes)}")


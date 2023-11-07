#!/usr/bin/python3

"""Write a Python program to print the number of prime numbers that are less than or equal to a given number.
Input:
n (1 <= n <= 999,999)
Input the number(n): 35
Number of prime numbers which are less than or equal to n.: 11"""

def isPrime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2: # Prime is only divisible by 1 and the number itself
        return True
    return False

if __name__ == "__main__":
    n = int(input("\n Input the number(n): "))
    count = 0
    for i in range(2,n+1):
        if isPrime(i):
            count += 1
    print(" Number of prime numbers which are less than or equal to n.:",count)
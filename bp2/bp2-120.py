#!/usr/bin/python3

"""Write a Python program to check if two given numbers are Co Prime or not. 
Return True if two numbers are Co Prime otherwise return false.
Sample Input:
(17, 13)
(17, 21)
(15, 21)
(25, 45)
Sample Output:
True
True
False
False"""

# from math import sqrt

# def getDiv(num):
#     divisors = []
#     for i in range(2,int(sqrt(num))+1):
#         if num % i == 0:
#             if num / i == i:
#                 divisors.append(i)
#             else:
#                 divisors.append(i)
#                 divisors.append(int(num/i))
#     return divisors

# def checkCoPrime(a,b):
#     return False if any([i in getDiv(a) for i in getDiv(b)]) else True

# OR

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def checkCoPrime(a,b):
    return gcd(max(a,b),min(a,b)) == 1

if __name__ == "__main__":
    print(checkCoPrime(17, 13))
    print(checkCoPrime(17, 21))
    print(checkCoPrime(15, 21))
    print(checkCoPrime(25, 45))
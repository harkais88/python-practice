#!/usr/bin/python3

"""Write a Python program to calculate Euclid's totient function for a given integer. 
Use a primitive method to calculate Euclid's totient function.
Sample Input:
(10)
(15)
(33)
Sample Output:
4
8
20"""

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def totient(num):
    phi = 1
    for i in range(2,num):
        if gcd(num,i) == 1:
            phi += 1
    return phi

if __name__ == "__main__":
    print(totient(10))
    print(totient(15))
    print(totient(33))
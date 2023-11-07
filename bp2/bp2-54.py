#!/usr/bin/python3

"""Write a Python program which accepts an even number (>=4, Goldbach number) 
from the user and creates combinations which express the given number as a 
sum of two prime numbers. Print the number of combinations.
Goldbach number: A Goldbach number is a positive even integer that can be 
expressed as the sum of two odd primes. Since four is the only even number 
greater than two that requires the even prime 2 in order to be written as the 
sum of two primes, another form of the statement of Goldbach's conjecture is that 
all even integers greater than 4 are Goldbach numbers.
The expression of a given even number as a sum of two primes is called a 
Goldbach partition of that number. The following are examples of Goldbach partitions for some even numbers:
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
...
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
Input an even number:
100
Number of combinations:
6"""

from itertools import combinations
from math import sqrt

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Input an even number:\n"))
    if n % 2 == 0:
        goldbach_count = 0
        combs = list(combinations(range(n+1),2))
        prime_combs = []
        for ele in combs:
            if isPrime(ele[0]) and isPrime(ele[1]):
                prime_combs.append(ele)
        print(f"{n} = ",end="")
        for ele in prime_combs:
            if ele[0] + ele[1] == n:
                goldbach_count += 1
        print(f"\nNumber of combinations:\n{goldbach_count}")
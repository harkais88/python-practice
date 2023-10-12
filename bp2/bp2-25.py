#!/usr/bin/python3

"""Write a Python program to find the total number of even or odd divisors of a given integer."""

from math import sqrt

def divCount(num):
    divisors = []
    odd_count = 0
    even_count = 0
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            if (num / i == i):
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(num/i))
    
    for i in range(len(divisors)):
        if divisors[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print()
    print(f"Divisors of {num}: {sorted(divisors)}")
    print(f"Number of Odd Divisors of {num}: {odd_count}")        
    print(f"Number of Even Divisors of {num}: {even_count}")        

if __name__ == "__main__":
    divCount(100)
    divCount(1234)
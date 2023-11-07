#!/usr/bin/python3

"""Write a Python program that reads an integer n and finds the number of 
combinations of a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n.
Input:
n (1 <= n <= 50)
Input the number(n): 15
Number of combinations: 592"""

import itertools

def noOfCombs(n):
    count = 0

    # for a,b,c,d in itertools.product(range(10),range(10),range(10),range(10)):
    #     count += (a+b+c+d == n)

    # OR
    
    # Much shorter loop
    for a,b,c in itertools.product(range(10),range(10),range(10)): 
        count += (0 <= n - (a+b+c) <= 9)

    return count

if __name__ == "__main__":
    n = int(input("\n Enter the number: "))
    print(" Number of combinations: ",noOfCombs(n))
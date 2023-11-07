#!/usr/bin/python3

"""From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the 
sum of the squares of its digits, and repeat the process until 
the number equals 1 (where it will stay), or it loops endlessly 
in a cycle which does not include 1. Those numbers for which this 
process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to check whether a number is "happy" or not.
Sample Input:
(7)
(932)
(6)
Sample Output:
True
True
False"""

from math import pow

def isHappy(num):
    touched = [num]
    count = 0

    while True:
        count += 1
        sum = 0
        n = touched[-1]
        while n != 0:
            sum += pow(n % 10,2)
            n = n // 10        
        if sum in touched:
            break
        if sum == 1:
            break
        touched.append(sum)

    if sum == 1:
        print(num," is a happy number")
    else:
        print(num," is not a happy number")
    print(count)

if __name__ == "__main__":
    isHappy(7)
    isHappy(932)
    isHappy(6)
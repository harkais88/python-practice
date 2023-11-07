#!/usr/bin/python3

"""From Wikipedia,
A happy number is defined by the following process:
Starting with any positive integer, replace the number 
by the sum of the squares of its digits, and repeat the 
process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy 
numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to find and print the first 10 happy numbers.
Sample Input:
[:10]
Sample Output:
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44]"""

def isHappy(num,happy_nums):
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
        if sum == 1 or sum in happy_nums:
            break
        touched.append(sum)

    print(f"For num {num} = {count}")
    if sum == 1 or sum in happy_nums:
        return True
    return False

def getHappynums(max):
    num = 1
    happy_nums = []

    while len(happy_nums) < max:
        if isHappy(num,happy_nums):
            happy_nums.append(num)
        num += 1

    return happy_nums

if __name__ == "__main__":
    print(getHappynums(10))
    print(getHappynums(100))
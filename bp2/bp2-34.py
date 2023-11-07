#!/usr/bin/python3

"""Write a Python program to compute the digit number of the sum of two given integers.
Input:
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 <= x, y <= 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2"""

if __name__ == "__main__":
    print("Input two integers(a b):")
    a,b = [int(i) for i in input().split()]

    sum = a+b

    print("Sum of two integers a and b.:")
    print(sum % 10)
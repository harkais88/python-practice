#!/usr/bin/python3

"""Write a Python program to find the maximum sum of a contiguous subsequence 
from a given sequence of numbers a1, a2, a3, ... an. 
A subsequence of one element is also a continuous subsequence.
Input:
You can assume that 1 <= n <= 5000 and -100000 <= ai <= 100000.
Input numbers are separated by a space.
Input 0 to exit.
Input number of sequence of numbers you want to input (0 to exit):
3
Input numbers:
2
4
6
Maximum sum of the said contiguous subsequence: 12
Input number of sequence of numbers you want to input (0 to exit):
0"""

# To clarify, some contiguous subsequences of [1,-5,2,-1,3] are
# [1], [-5,2] and [2,1,3], and [1,2,3] is not a contiguous subsequence of [1,-5,2,-1,3], even if it is
# a sequence
# So the challenge here is to find the maximum possible sum from a contiguous subsequence

# Based on Kadane's algorithm

from sys import maxsize

if __name__ == "__main__":
    while True:
        n = int(input("Input number of sequence of numbers you want to input (0 to exit):\n"))

        if n == 0:
            break

        li = []
        print("Input numbers:")
        for i in range(n):
            li.append(int(input()))

        max_so_far = -maxsize -1
        max_ending_here = 0
        # For getting the continguous sequence with the maximum sum
        s = start = end = 0

        for i in range(n):
            max_ending_here += li[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                start = s
                end = i
            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1

        print("Maximum sum of the said contiguous subsequence:",max_so_far)
        print("Contiguous Sequence with Maximum Sum: ",li[start:end+1])
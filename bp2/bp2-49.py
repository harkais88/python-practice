#!/usr/bin/python3

"""Write a Python program that reads n digits (given) chosen from 0 to 9 
and prints the number of combinations where the sum of the digits equals 
another given number (s). Do not use the same digits in a combination.
Input:
Two integers as number of combinations and their sum by a single space in a line.
Input number of combinations and sum:
2 4
2
HINT: Use combinations from itertools
"""

# We can easily do this using the combinations class from itertools for this purpose

from itertools import combinations

if __name__ == "__main__":
    print("Input number of combinations and sum, input 0 0 to exit:")
    result = 0
    c,s = [int(i) for i in input().split()]
    combs = combinations(range(10),c)
    for comb in combs:
        if sum(comb) == s:
            result += 1

    print(f"Number of combinations of {c} digits with sum = {s}: {result}")
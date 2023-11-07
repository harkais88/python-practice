#!/usr/bin/python3

"""Write a Python program to find the number of combinations that satisfy p + q + r + s = n 
where n is a given number <= 4000 and p, q, r, s are between 0 to 1000.
Input a positive integer:
252
Number of combinations of a,b,c,d: 2731135"""

from collections import Counter

if __name__ == "__main__":
    n = int(input("Input a positive integer: "))

    pair_dict = Counter()
    for i in range(2001):
        pair_dict[i] = min(i,2000-i) + 1

    no_of_combs = 0
    for i in range(n+1):
        print("Iteration",i+1)
        print(f"pair_dict[{i}] = {pair_dict[i]}, pair_dict[{n-i}] = {pair_dict[n-i]}")
        print(f"no_of_combs now = {no_of_combs}")
        no_of_combs += pair_dict[i] * pair_dict[n-i]

    print("Number of combinations of a,b,c,d: ",no_of_combs)
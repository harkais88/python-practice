#!/usr/bin/python3

"""Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values."""

from random import randint

def chckPair(list):
    pairs = []
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]*list[j] % 2 != 0) and (list[i], list[j]) not in pairs and (list[j], list[i]) not in pairs:
                pairs.append((list[i],list[j]))
    return pairs

if __name__ == "__main__":
    list = [randint(1,9) for _ in range(10)]

    print(" Generated List: ",list)
    print(" Distinct pairs found in list whose product is odd: ",chckPair(list))
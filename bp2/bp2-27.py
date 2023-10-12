#!/usr/bin/python3

"""Write a Python program to compute the summation of the absolute difference of all distinct 
pairs in a given array (non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3"""

from itertools import permutations

def sumOfDistinctPairs(arr):
    abs_pairs = set([tuple(sorted(i)) for i in permutations(arr,2)])
    sum = 0
    for ele1,ele2 in abs_pairs:
        sum += abs(ele1-ele2)
    print(" Sum of the absolute differences of all distinct pairs: ",sum)

if __name__ == "__main__":
    sumOfDistinctPairs([1,2,3])
    sumOfDistinctPairs([1,4,5])


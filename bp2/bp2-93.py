#!/usr/bin/python3

"""Write a Python program to compute the cumulative sum of numbers in a given list.
Note: Cumulative sum = sum of itself + all previous numbers in the said list.
Sample Input:
[10, 20, 30, 40, 50, 60, 7]
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
Sample Output:
[10, 30, 60, 100, 150, 210, 217]
[1, 3, 6, 10, 15]
[0, 1, 3, 6, 10, 15]"""

def cumulativeSum(list):
    return [sum(list[:i+1]) for i in range(len(list))]

if __name__ == "__main__":
    print(cumulativeSum([10, 20, 30, 40, 50, 60, 7]))
    print(cumulativeSum([1, 2, 3, 4, 5]))
    print(cumulativeSum([0, 1, 2, 3, 4, 5]))
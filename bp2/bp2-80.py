#!/usr/bin/python3

"""Write a Python program to compute the largest product of three integers from a given list of integers.
Sample Input:
[-10, -20, 20, 1]
[-1, -1, 4, 2, 1]
[1, 2, 3, 4, 5, 6]
Sample Output:
4000
8
120"""

def getMaxProd(list):
    max_prod = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for k in range(j+1,len(list)):
                max_prod = max(list[i] * list[j] * list[k], max_prod)
    return max_prod

if __name__ == "__main__":
    print(getMaxProd([-10, -20, 20, 1]))
    print(getMaxProd([-1, -1, 4, 2, 1]))
    print(getMaxProd([1, 2, 3, 4, 5, 6]))
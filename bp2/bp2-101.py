#!/usr/bin/python3

"""Write a Python program to compute the sum of all items in a 
given array of integers where each integer is multiplied by its index. Return 0 if there is no number.
Sample Input:
[1,2,3,4]
[-1,-2,-3,-4]
[]
Sample Output:
20
-20
0"""

def sumOfIndexMultipliedInts(list):
    if len(list) == 0:
        return 0
    
    return sum([list[i] * i for i in range(len(list))])

if __name__ == "__main__":
    print(sumOfIndexMultipliedInts([1,2,3,4]))
    print(sumOfIndexMultipliedInts([-1,-2,-3,-4]))
    print(sumOfIndexMultipliedInts([]))
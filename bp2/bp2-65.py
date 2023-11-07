#!/usr/bin/python3

"""Given a list of numbers and a number k, write a Python program to check 
whether the sum of any two numbers from the list is equal to k or not.
For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
Sample Input:
([12, 5, 0, 5], 10)
([20, 20, 4, 5], 40)
([1, -1], 0)
([1, 1, 0], 0)
Sample Output:
True
True
True
False"""

def checkSum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False

if __name__ == "__main__":
    print(checkSum([12, 5, 0, 5], 10))
    print(checkSum([20, 20, 4, 5], 40))
    print(checkSum([1, -1], 0))
    print(checkSum([1, 1, 0], 0))
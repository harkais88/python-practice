#!/usr/bin/python3

"""Write a Python program to remove duplicate numbers from a given list of numbers.
Sample Input:
([1,2,3,2,3,4,5])
([1,2,3,2,4,5])
([1,2,3,4,5])
Sample Output:
Original list of numbers: [1, 2, 3, 2, 3, 4, 5]
After removing the duplicate numbers from the said list:
[1, 4, 5]
Original list of numbers: [1, 2, 3, 2, 4, 5]
After removing the duplicate numbers from the said list:
[1, 3, 4, 5]
Original list of numbers: [1, 2, 3, 4, 5]
After removing the duplicate numbers from the said list:
[1, 2, 3, 4, 5]"""

def rmvDups(nums):
    print("Original list of numbers: ",nums)
    print("After removing the duplicate numbers from the said list:")
    print([i for i in nums if nums.count(i) == 1])

if __name__ == "__main__":
    rmvDups([1, 2, 3, 2, 3, 4, 5])
    rmvDups([1, 2, 3, 2, 4, 5])
    rmvDups([1, 2, 3, 4, 5])
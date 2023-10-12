#!/usr/bin/python3

"""Write a Python program to identify unique triplets whose three elements 
sum to zero from an array of n integers."""

from random import randint

if __name__ == "__main__":
    nums = [randint(-10,10) for _ in range(20)]

    result = []

    print("Identifying unique triplets whose sum is zero in list ",nums,": ",end="")

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = tuple(sorted((nums[i],nums[j],nums[k])))
                    if triplets not in result:
                        result.append(triplets)
        
    print(result)
#!/usr/bin/python3

"""Write a NumPy program to convert a given list into an array, 
then again convert it into a list. Check initial list and final list are equal or not."""

import numpy as np

if __name__ == "__main__":
    nums = [1,2,3,4]
    print("List given: ",nums)
    nums_arr = np.array(nums)
    print("List in array form: ",nums_arr)
    nums_arr = nums_arr.tolist()
    print("Array back in list form: ",nums_arr)
    print("Are they equal? ",nums == nums_arr)
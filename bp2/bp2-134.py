#!/usr/bin/python3

"""Write a Python program to compute the sum of the negative and 
positive numbers in an array of integers and display the largest sum.
Original array elements: {0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20}
Largest sum - Positive/Negative numbers of the said array: 105
Original array elements: {0, 3, 4, 5, 9, -22, -44, -11}
Largest sum - Positive/Negative numbers of the said array: -77"""

def returnLargestSum(nums):
    print("Original array elements ",nums)
    print("Largest sum - Positive/Negative numbers of the said array: ",end = "")
    pos_sum = sum([i for i in nums if i >= 0])
    neg_sum = sum([i for i in nums if i < 0])
    #print(neg_sum if abs(neg_sum) > pos_sum else pos_sum)
    #OR
    print(max(pos_sum,neg_sum,key=abs))

if __name__ == "__main__":
    returnLargestSum({0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20})
    returnLargestSum({0, 3, 4, 5, 9, -22, -44, -11})
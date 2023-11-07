#!/usr/bin/python3

"""Write a Python program that accepts a list of numbers. Count the negative 
numbers and compute the sum of the positive numbers of the said list. Return these values through a list.
Original list: [1, 2, 3, 4, 5]
Number of negative of numbers and sum of the positive numbers of the said list: [0, 15]
Original list: [-1, -2, -3, -4, -5]
[5, 0]
Number of negative of numbers and sum of the positive numbers of the said list: [5, 0]
Original list: [1, 2, 3, -4, -5]
[2, 6]
Number of negative of numbers and sum of the positive numbers of the said list: [2, 6]
Original list: [1, 2, -3, -4, -5]
[3, 3]
Number of negative of numbers and sum of the positive numbers of the said list: [3, 3]"""

def countNegAndCalcSum(list):
    print("Original list: ",list)
    print("Number of negative of numbers and sum of the positive numbers of the said list: ",
          [len([i for i in list if i < 0]), sum([i for i in list if i > 0])])

if __name__ == "__main__":
    countNegAndCalcSum([1,2,3,4,5])
    countNegAndCalcSum([-1,-2,-3,-4,-5])
    countNegAndCalcSum([1,2,3,-4,-5])
    countNegAndCalcSum([1,2,-3,-4,-5])
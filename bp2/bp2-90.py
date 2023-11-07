#!/usr/bin/python3

"""Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers.
Original list of numbers: [10, 20, 30, 40, 50, 60, 7]
Sum of the three lowest positive numbers of the said array: 37
Original list of numbers: [1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6
Original list of numbers: [0, 1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6"""

def getSumOfLowThree(list):
    print("Original list of numbers: ",list)
    list = [ele for ele in sorted(list) if ele > 0]
    print("Sum of the three lowest positive numbers of the said array: ",sum([list[0],list[1],list[2]]))

if __name__ == "__main__":
    getSumOfLowThree([10, 20, 30, 40, 50, 60, 7])
    getSumOfLowThree([1, 2, 3, 4, 5])
    getSumOfLowThree([0, 1, 2, 3, 4, 5])
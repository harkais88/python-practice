#!/usr/bin/python3

"""Write a Python program to find the largest product of a pair of adjacent 
elements from a given list of integers.
Original list: [1, 2, 3, 4, 5, 6]
Largest product of the pair of adjacent elements of the said list: 30
Original list: [1, 2, 3, 4, 5]
Largest product of the pair of adjacent elements of the said list: 20
Original list: [2, 3]
Largest product of the pair of adjacent elements of the said list: 6"""

def getLargestProd(list):
    print("Original List: ",list)
    print("Largest product of the pair of adjacent elements of the said list: ",end="")
    print(max([list[i] * list[i-1] for i in range(1,len(list))]))

if __name__ == "__main__":
    getLargestProd([1,2,3,4,5,6])
    getLargestProd([1,2,3,4,5])
    getLargestProd([2,3])
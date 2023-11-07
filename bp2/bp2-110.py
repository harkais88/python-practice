#!/usr/bin/python3

"""Write a Python program to find the indices of all occurrences of a given item in a given list.
Sample Input:
([1,2,3,4,5,2], 2)
([3,1,2,3,4,5,6,3,3], 3)
([1,2,3,-4,5,2,-4], -4)
Sample Output:
Original list of numbers: [1, 2, 3, 4, 5, 2]
Given Number 2
Indices of all occurrences of the said item in the given list:
[1, 5]
Original list of numbers: [3, 1, 2, 3, 4, 5, 6, 3, 3]
Given Number 3
Indices of all occurrences of the said item in the given list:
[0, 3, 7, 8]
Original list of numbers: [1, 2, 3, -4, 5, 2, -4]
Given Number -4
Indices of all occurrences of the said item in the given list:
[3, 6]
Original list of numbers: [1, 2, 3, 4, 5, 2]
Given Number 7
Indices of all occurrences of the said item in the given list:
[]"""

def getIndices(list,num):
    print("Original list of numbers: ",list)
    print("Given Number ",num)
    print([i[0] for i in enumerate(list) if i[1] == num])

if __name__ == "__main__":
    getIndices([1, 2, 3, 4, 5, 2],2)
    getIndices([3, 1, 2, 3, 4, 5, 6, 3, 3],3)
    getIndices([1, 2, 3, -4, 5, 2, -4],-4)
    getIndices([1, 2, 3, 4, 5, 2],7)
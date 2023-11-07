#!/usr/bin/python3

"""Write a Python program to find the first missing positive integer that does not exist in a given list.
Sample Input:
[2, 3, 7, 6, 8, -1, -10, 15, 16]
[1, 2, 4, -7, 6, 8, 1, -10, 15]
[1, 2, 3, 4, 5, 6, 7]
[-2, -3, -1, 1, 2, 3]
Sample Output:
4
3
8
4"""

def getFirstMissPosInt(list):
    index = 0

    while index < len(list):
        if list[index] > 0:
            i = list[index]
            while True:
                if index == len(list):
                    break
                if i != list[index]:
                    return i
                i += 1
                index += 1
        index += 1

    return i

if __name__ == "__main__":
    print(getFirstMissPosInt([2, 3, 7, 6, 8, -1, -10, 15, 16]))
    print(getFirstMissPosInt([1, 2, 4, -7, 6, 8, 1, -10, 15]))
    print(getFirstMissPosInt([1, 2, 3, 4, 5, 6, 7]))
    print(getFirstMissPosInt([-2, -3, -1, 1, 2, 3]))
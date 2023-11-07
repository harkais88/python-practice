#!/usr/bin/python3

"""Write a Python program to find the starting and ending position of 
a given value in a given array of integers, sorted in ascending order.
If the target is not found in the array, return [0, 0].
Input: [5, 7, 7, 8, 8, 8] target value = 8
Output: [3, 5]
Input: [1, 3, 6, 9, 13, 14] target value = 4
Output: [0, 0]
Input: [73, 25, 13, 19, 49, 74, 49, 5, 37, 20] target value = 49
Output: [6, 7]"""

from random import randint

# Using quicksort 
def sort(list):
    if len(list) == 0:
        return []
    
    pivot = len(list) - 1
    i = -1
    j = 0

    while j != pivot:
        if list[j] < list[pivot]:
            i += 1
            list[i],list[j] = list[j],list[i]
        j += 1
    i += 1
    list[i],list[pivot] = list[pivot],list[i]
    list = sort(list[:i]) + [list[i]] + sort(list[i+1:])

    return list

def startAndEndPosOfTarget(arr,target):
    arr = sort(arr)
    print("Sorted array: ",arr)
    start_pos = 0 
    end_pos = 0

    for i in range(len(arr)):
        if arr[i] == target and start_pos == 0:
            start_pos = i
            end_pos = i
        elif arr[i] == target and start_pos != 0:
            end_pos = i

    return [start_pos,end_pos]

if __name__ == "__main__":
    arr = [randint(1,100) for _ in range(10)]
    target = randint(0,9)

    print(f"Input: {arr} target value = {arr[target]}")
    print(f"Output: {startAndEndPosOfTarget(arr,arr[target])}")


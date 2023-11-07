#!/usr/bin/python3

"""Write a Python program to convert all items in a given list to float values.
Original list:
['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', 
'0.54', '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
List of Floats:
[0.49, 0.54, 0.54, 0.54, 0.54, 0.54, 0.55, 0.54, 0.54, 0.54, 
0.55, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]"""

def toFloat(nums):
    print(f"Original list:\n{nums}")
    print("List of Floats:")
    print(list(map(float,nums)))

if __name__ == "__main__":
    toFloat(['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', 
             '0.54', '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54'])

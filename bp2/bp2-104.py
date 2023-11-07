#!/usr/bin/python3

"""Write a Python program to check whether two given lines are parallel or not.
Note: Parallel lines are two or more lines that never intersect. 
Parallel Lines are like railroad tracks that never intersect.
The General Form of the equation of a straight line is: ax + by = c
The said straight line is represented in a list as [a, b, c]
Example of two parallel lines:
x + 4y = 10 and x + 4y = 14
Sample Input:
([2,3,4], [2,3,8])
([2,3,4], [4,-3,8])
Sample Output:
True
False"""

# Two lines are parallel if their slopes are equal
# y = mx + c => m = (y - c / x)

def isParallel(line1, line2):
    return line1[1] / line1[0] == line2[1] / line2[0]

if __name__ == "__main__":
    print(isParallel([2,3,4], [2,3,8]))
    print(isParallel([2,3,4], [4,-3,8]))
    
#!/usr/bin/python3

"""Write a Python program which checks whether two circles in the same plane 
(with the same center (x,y) and radius) intersect. If intersection occurs, return true, otherwise return false.
Sample Input:
([1,2, 4], [1,2, 8])
([0,0, 2], [10,10, 5])
Sample Output:
True
False"""

from math import sqrt,pow

def circleIntersect(circle1, circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    return sqrt(pow((x2 - x1),2) + pow((y2 - y1),2)) < r1 + r2

if __name__ == "__main__":
    print(circleIntersect([1,2, 4], [1,2, 8]))
    print(circleIntersect([0,0, 2], [10,10, 5]))
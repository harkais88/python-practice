#!/usr/bin/python3

""" Write a Python program to check if a point (x,y) is in a triangle or not. A triangle is formed by three points.
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space.
 2 3 4 5 6 8 7 1
The point is outside the triangle."""

from math import sqrt

def triangleArea(x1,y1,x2,y2,x3,y3):
    A = (1/2) * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

    if A <= 0:
        print("Given Coordinates do not form valid triangle")
        return -1
    else:
        return A

if __name__ == "__main__":
    x1,y1,x2,y2,x3,y3,xp,yp = [float(i) for i in 
                               input("Input:\nx1,y1,x2,y2,x3,y3,xp,yp separated by a single space.\n").split()]
    
    if triangleArea(x1,y1,x2,y2,x3,y3) != -1:
        if ( triangleArea(xp,yp,x2,y2,x3,y3) + 
             triangleArea(x1,y1,xp,yp,x3,y3) + 
             triangleArea(x1,y1,x2,y2,xp,yp) ) == triangleArea(x1,y1,x2,y2,x3,y3):
            print("The point is inside the triangle.")
        else:
            print("The point is outside the triangle.")     

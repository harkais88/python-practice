#!/usr/bin/python3

"""Write a Python program to test whether two lines PQ and RS are parallel. 
The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
Input:
x1,y1,x2,y2,x3,y3,x4,y4 separated by a single space
Input x1,y1,x2,y2,x3,y3,x4,y4:
2 5 6 4 8 3 9 7
PQ and RS are not parallel"""

from math import sqrt

if __name__ == "__main__":
    print("The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).")
    print("x1,y1,x2,y2,x3,y3,xp,yp separated by a single space")
    x1,y1,x2,y2,x3,y3,x4,y4 = [int(i) for i in input("Input x1,y1,x2,y2,x3,y3,x4,y4:").split()]

    # One way to do it
    # def length(x1,y1,x2,y2):
    #     return sqrt((x2-x1)**2 + (y2-y1)**2)

    # if length(x1,y1,x2,y2) == length(x3,y3,x4,y4) and length(x1,y1,x3,y3) == length(x2,y2,x4,y4):
    #     print("PQ and RS are parallel")
    # else:
    #     print("PQ and RS are not parallel")

    # Another way, and probably the straightforward way to do it
    m1 = (y2 - y1) / (x2 - x1) # Slope of PQ
    m2 = (y4 - y3) / (x4 - x3) # Slope of RS

    if m1 == m2:
        print("PQ and RS are parallel")
    else:
        print("PQ and RS are not parallel")
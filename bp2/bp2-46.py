#!/usr/bin/python3

"""There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 
and central coordinate (x2, y2).

Write a Python program to test the followings -

"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect
"C1 and C2 do not overlap" if C1 and C2 do not overlap and
"Circumference of C1 and C2 will touch" if C1 and C2 touch

Input:
Input numbers (real numbers) are separated by a space.
Input x1, y1, r1, x2, y2, r2:
5 4 2 3 9 2
C1 and C2 do not overlap
Input x1, y1, r1, x2, y2, r2:
5 4 3 5 10 3
Circumference of C1 and C2 will touch
Input x1, y1, r1, x2, y2, r2:
6 4 3 10 4 2
Circumference of C1 and C2 intersect
Input x1, y1, r1, x2, y2, r2:
5 4 3 5 4 2
C2 is in C1
Input x1, y1, r1, x2, y2, r2:
5 4 2 5 4 3
C1 is in C2"""

# These are geometrical observations, do that one yourself

from math import sqrt

if __name__ == "__main__":
    x1,y1,r1,x2,y2,r2 = [int(i) for i in input("Input x1, y1, r1, x2, y2, r2:\n").split()]

    distance = sqrt((x2-x1)**2 + (y2-y1)**2)

    if distance <= r2 - r1:
        print("C1 is in C2")
    elif distance <= r1 - r2:
        print("C2 is in C1")
    elif distance == r1 + r2:
        print("Circumference of C1 and C2 will touch")
    elif distance < r1 + r2:
        print("Circumference of C1 and C2 intersect")
    else:
        print("C1 and C2 do not overlap")
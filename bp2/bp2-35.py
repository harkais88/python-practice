#!/usr/bin/python3

"""Write a Python program to check whether three given lengths (integers) of three sides 
form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
Input:
Integers separated by a single space.
1 <= length of the side <= 1,000
Input three integers(sides of a triangle)
8 6 7
No"""

def checkRightTriangle(a,b,c):
    return (a**2 + b**2 == c**2 or
            b**2 + c**2 == a**2 or
            c**2 + a**2 == b**2) 

if __name__ == "__main__":
    print("Input three integers(sides of a triangle)")
    a,b,c = [int(i) for i in input().split()]
    if checkRightTriangle(a,b,c):
        print("Yes")
    else:
        print("No") 
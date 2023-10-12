#!/usr/bin/python3

"""Write a Python program to get the third side of a right-angled triangle from two given sides."""

from math import sqrt,pow

if __name__ == "__main__":
    side1 = float(input("\n Enter the length of one side of the right angled triangle: "))
    side2 = float(input("\n Enter the length of the other side: "))

    print("\n Length of the third side of the right angled triangle: ",sqrt(pow(side1,2) + pow(side2,2)))
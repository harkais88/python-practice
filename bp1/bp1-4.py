#!/usr/bin/python3

"""Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504"""

from math import pi

if __name__ == "__main__":
    radius = float(input("\n Enter the radius of the circle: "))

    area = pi * radius * radius

    print("\n Area of the circle: ",area)
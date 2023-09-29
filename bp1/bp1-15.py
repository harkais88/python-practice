#!/usr/bin/python3

"""Write a Python program to get the volume of a sphere with radius six."""

from math import pi,pow

if __name__ == "__main__":
    radius = float(input("\n Enter the radius of the sphere: "))

    print("\n Volume of the sphere: ", (4/3)*pi*pow(radius,3))
#!/usr/bin/python3

"""Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)."""

from math import sqrt

if __name__ == "__main__":
    x1,y1 = [float(i) for i in input("\n Enter the coordinates in format x1,y1: ").split(",")]
    x2,y2 = [float(i) for i in input("\n Enter the coordinates in format x2,y2: ").split(",")]

    #Considering Euclidian Distance
    print("\n The distance between {},{} and {},{} is {} units".format(x1,y1, x2,y2, sqrt((x2 - x1)**2 + 
                                                                                          (y2 - y1)**2)))

    
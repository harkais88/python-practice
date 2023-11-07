#!/usr/bin/python3

"""A convex polygon is a simple polygon in which no line segment between two points 
on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon 
whose interior is a convex set. In a convex polygon, all interior angles are less than 
or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly 
less than 180 degrees. Write a Python program that compute the area of the polygon . The 
vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order 
of edge connections
Input:
Input number of sides: 5
Side: 1
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 0
Side: 2
Input the Coordinate:
Input Coordinate x: 0
Input Coordinate y: 0
Side: 3
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 1
Side: 4
Input the Coordinate:
Input Coordinate x: 2
Input Coordinate y: 0
Side: 5
Input the Coordinate:
Input Coordinate x: -1
Input Coordinate y: 1
Area of the Polygon: 0.5"""

def calcArea(coords):
    coords.append(coords[0])
    print(coords)
    area = 0
    for coord_index in range(len(coords)-1):
        area += (coords[coord_index][0]*coords[coord_index+1][1]) - (coords[coord_index][1]*coords[coord_index+1][0])
    return abs(area) / 2

if __name__ == "__main__":
    n = int(input("Input number of sides: "))
    coords = []
    for i in range(n):
        print("Side ",i+1)
        coords.append((int(input("Input Coordinate x: ")),int(input("Input Coordinate y: "))))
    print("Area of the Polygon: ",calcArea(coords))
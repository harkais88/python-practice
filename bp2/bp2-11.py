#!/usr/bin/python3

"""Write a Python program to check the sum of three elements (each from an array) from three arrays is equal 
to a target value. Print all those three-element combinations.
Sample data:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
*/"""

from itertools import product

if __name__ == "__main__":
    X = [10,20,20,20]
    Y = [10,20,30,40]
    Z = [10,30,40,20]

    target = 70

    print(f" Printing all 3-value combinations from the arrays {X}, {Y}, {Z} equal to the target {target}: ",end="")

    for values in list(product(X,Y,Z)):
        x,y,z = values
        if (x + y + z == target):
            print(values, end = " ")
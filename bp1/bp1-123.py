#!/usr/bin/python3

"""Write a Python program to empty a variable without destroying it.

Sample data: 
n=20
d = {"x":200}
Expected Output : 
0
{}"""

if __name__ == "__main__":
    n = 20
    d = {"x":200}
    print(type(n)()) # Equivalent of int(), which would return 0
    print(type(d)())
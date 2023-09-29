#!/usr/bin/python3

"""Write a Python program to input two integers on a single line. """

if __name__ == "__main__":
    # One way to do it
    # x,y = map(int, input("\n Enter two integers: ").split())

    # Another way to do it
    x,y = [int(a) for a in input("\n Enter two integers: ").split()]

    print(" The integers: ",x,y)

#!/usr/bin/python3

"""Write a Python program to swap two variables."""

if __name__ == "__main__":
    a,b = [int(i) for i in input("\n Enter two variables seperated by commas: ").split(",")]

    print("\n Original Variables: a = {0}, b = {1}".format(a,b))

    #Probably the best way to do this without adding extra stop
    a = a+b
    b = a-b
    a = a-b

    print("\n Swapped Variables: a = {0}, b = {1}".format(a,b))

    #Or we could do it with a temporary variable
    temp = a
    a = b
    b = temp

    print("\n Swapped Again Variables: a = {}, b = {}".format(a,b))
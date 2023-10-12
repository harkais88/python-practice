#!/usr/bin/python3

"""Write a Python program to convert numbers to 3 digit combinations.
Ex - 1 - 001, 11 - 011, 111 - 111"""

if __name__ == "__main__":
    print(" Numbers in 3-digit combinations: ")
    for i in range(0,1000):
        print("({},{}) ".format(i,str(i).zfill(3)),end="")
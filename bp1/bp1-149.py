#!/usr/bin/python3

"""Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number. """

if __name__ == "__main__":
    n = int(input("\n Enter an integer: "))

    sum = 0
    for i in range(1,n):
        sum += i**3

    print("Sum of the cube of all postive integers smaller than {}: {}".format(n,sum))
#!/usr/bin/python3

"""Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference."""

if __name__ == "__main__":
    n = float(input("\n Enter a number: "))

    print(" Result: ", 17 - n if n <= 17 else 2*abs(17 - n))
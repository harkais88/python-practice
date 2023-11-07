#!/usr/bin/python3

"""Write a Python program to compute and print the sum of two given integers (greater or equal to zero). 
In the event that the given integers or the sum exceed 80 digits, print "overflow".
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47"""

if __name__ == "__main__":
    n1 = int(input("Input first integer:\n"))
    n2 = int(input("Input second integer:\n"))

    if n1 >= 10**80 or n2 >= 10**80 or (n1+n2) >= 10**80:
        print("Overflow!")
    else:
        print(f"Sum of the two integers: {n1+n2}")
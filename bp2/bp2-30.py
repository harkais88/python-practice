#!/usr/bin/python3

"""Write a Python program to find common divisors between two numbers in a given pair."""

if __name__ == "__main__":
    n1 = int(input("\n Enter a number: "))
    n2 = int(input("\n Enter another number: "))

    div_count = 0
    for i in range(1,min(n1,n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            div_count += 1

    print("\n Number of common divisors between {} and {}: {}".format(n1,n2,div_count))
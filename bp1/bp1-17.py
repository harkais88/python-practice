#!/usr/bin/python3

"""Write a Python program to test whether a number is within 100 of 1000 or 2000."""

if __name__ == "__main__":
    n = int(input("\n Enter a number: "))

    print("\n Is the number within a 100 of 1000 or 2000? ", (n >= 1000 - 100 and n <= 1000 + 100) or \
                                                             (n >= 2000 - 100 and n <= 2000 + 100))
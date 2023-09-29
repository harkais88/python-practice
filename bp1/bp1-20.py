#!/usr/bin/python3

"""Write a Python program that returns a string that is n (non-negative integer) copies of a given string."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")
    n = abs(int(input("\n Enter the number of copies: ")))

    result = ""
    for i in range(n):
        result += string

    print("\n Result: ",result)
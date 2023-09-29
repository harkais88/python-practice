#!/usr/bin/python3

"""Write a Python program that accepts the user's first and last name and prints them in reverse order 
with a space between them."""

if __name__ == "__main__":
    first = input("\n Enter the first name: ")
    last = input("\n Enter the last name: ")

    print("\n Output: ",last[::-1]," ",first[::-1])
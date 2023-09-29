#!/usr/bin/python3

"""Write a Python program to add leading zeroes to a string. """

if __name__ == "__main__":
    str = "123.23"

    # Adding leading zeroes to str
    print("With leading zeroes: ", str.rjust(len(str)+4, "0"))

    # Adding trailing zeroes to str
    print("With trailing zeroes: ",str.ljust(len(str)+10, "0"))
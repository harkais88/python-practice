#!/usr/bin/python3

"""Write a Python program to format a specified string and limit the length of a string. """

if __name__ == "__main__":
    str = "The quick brown fox jumps over the lazy dog"

    print("Original String: ",str)
    print("Formatted Strings: {0:.12}\n\t\t{0:.24}\n\t\t{0:.9}".format(str))
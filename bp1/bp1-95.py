#!/usr/bin/python3

"""Write a Python program to convert the ASCII of each character in a given string to a list of integers."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")

    list = []

    for ele in string:
        list.append(ord(ele))

    print("\n List of the ASCII values of each character in {}: {}".format(string,list))
#!/usr/bin/python3

"""Write a Python program to count the number 4 in a given list."""

if __name__ == "__main__":
    list = input("\n Enter numbers: ").split(",")

    count = 0

    for i in list:
        if i == 4 or i == "4":
            count += 1

    print("\n Number of 4s in given list: ",count)

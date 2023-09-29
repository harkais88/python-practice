#!/usr/bin/python3

"""Write a Python program to remove the first item from a specified list. """

if __name__ == "__main__":
    list = ["Red", "Black", "Green", "Blue", "Red", "Yellow"]

    print("Before deleting the first item: ",list)
    list.remove(list[0])
    print("After deleting the first item: ",list)
#!/usr/bin/python3

"""Write a Python program that displays your name, age, and address on three different lines."""

if __name__ == "__main__":
    name = input("\n Enter your name: ")
    age = int(input("\n Enter your age: "))
    address = input("\n Enter your Address: ")

    print("\n Name: {} \n Age: {} \n Address: {}".format(name,age,address))
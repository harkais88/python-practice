#!/usr/bin/python3

"""Write a Python program that inputs a number and generates an error message if it is not a number. """

if __name__ == "__main__":
    num = input("\n Enter a number: ")
    
    try:
        num = int(num)
        print(" Huh, ",num," is a number!")
    except ValueError:
        print(" Yeah, ",num," is not a number....")
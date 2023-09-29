#!/usr/bin/python3

"""Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user. """

if __name__ == "__main__":
    x,y = map(int, input("Enter two integers: ").split())

    if max(x,y) % min(x,y) == 0:
        print(max(x,y) ,"is divisible by",min(x,y))
    else:
        print(max(x,y) ,"is not divisible by",min(x,y))
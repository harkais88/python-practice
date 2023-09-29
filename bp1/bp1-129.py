#!/usr/bin/python3

"""Write a Python program to check whether lowercase letters exist in a string. """

def lowChck(str):
    for ele in str:
        if ele.islower():
            print(str, "has lowercase letters")
            return
    print(str, "has no lowercase letters")

if __name__ == "__main__":
    str = input("\n Enter a string: ")

    lowChck(str)

    #OR you could just use the any function
    if any(ele.islower() for ele in str):
        print(str, "has lowercase letters")
    else:
        print(str, "has no lowercase letters")
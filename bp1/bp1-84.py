#!/usr/bin/python3

"""Write a Python program to count the number of occurrences of a specific character in a string."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")
    while True:
        char = input("\n Enter a character: ").lower()
        if len(char) == 1:
            break
        print("\n Enter only one letter")

    #One way to do it
    sum = 0
    for ele in string.lower():
        if ele == char:
           sum += 1

    print("\n Number of '{}'s in {}: {}".format(char,string,sum)) 

    #Or 

    print("\n Number of '{}'s in {}: {}".format(char,string,string.lower().count(char)))
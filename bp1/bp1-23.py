#!/usr/bin/python3

"""Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")
    n = abs(int(input("\n Enter the number of copies: ")))

    print("\n Result: ",end="")
    if len(string) < 2:
        for _ in range(n):
            print(string,end = "")
    else:
        for _ in range(n):
            print(string[:2],end = "")
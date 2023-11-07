#!/usr/bin/python3

""" Write a Python program to sum all numerical values (positive integers) embedded in a sentence.
Input:
Sentences with positive integers are given over multiple lines. Each line is a character 
string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. 
However the input is 80 characters or less per line and the sum is 10,000 or less.
Input some text and numeric values ( to exit):
Sum of the numeric values: 80
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 17
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 10
None"""

if __name__ == "__main__":
    string = input("\nEnter some lines. Hit Enter to confirm:\n").split()

    sum = 0

    for ele in string:
        index = 0
        while index < len(ele):
            if ele[index].isdigit():
                num = ele[index]
                index += 1
                while True:
                    if index >= len(ele):
                        break
                    if not ele[index].isdigit():
                        break
                    num += ele[index]
                    index += 1
                sum += int(num)
            else:
                index += 1

    print("Sum of the numeric values:",sum)
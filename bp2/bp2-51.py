#!/usr/bin/python3

"""Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
Input:
English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line.
The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python"""

if __name__ == "__main__":
    string = input("Input a text with two words 'Python' and 'Java'\n").split()

    for i in range(len(string)):
        if "Python" in string[i]:
            n = string[i].find("Python")
            string[i] = string[i][:n] + "Java" + string[i][n+6:]
        elif "Java" in string[i]:
            n = string[i].find("Java")
            string[i] = string[i][:n] + "Python" + string[i][n+4:]

    print(" ".join(string))
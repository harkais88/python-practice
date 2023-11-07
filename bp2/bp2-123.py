#!/usr/bin/python3

"""Write a Python program to check if a given string contains only lowercase or uppercase characters.
Original string:  PHP
Are all lowercase or uppercase?
Yes, all characters are upper
Original string:  javascript
Are all lowercase or uppercase?
Yes, all characters are lower
Original string:  Javascript
Are all lowercase or uppercase?
Nope"""

def checkLowerOrUpper(string: str):
    print("Original string: ",string)
    print("Are all lowercase or uppercase?")
    if string.islower():
        print("Yes, all characters are lower")
    else:
        print("Yes, all characters are upper" if string.isupper() else "Nope")

if __name__ == "__main__":
    checkLowerOrUpper("PHP")
    checkLowerOrUpper("javascript")
    checkLowerOrUpper("Javascript")
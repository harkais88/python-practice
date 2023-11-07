#!/usr/bin/python3

"""Write a Python program that replaces all but the last five 
characters of a string with "*" and returns the modified string.
Original String: kdi39323swe
new string: ******23swe
Original String: 12345abcdef
new string: ******bcdef
Original String: 12345
new string: 12345"""

def getModifiedString(string):
    print("Original String: ",string)
    print("New String: ", "*****" + string[len(string)-5:] if len(string) > 5 else string)

if __name__ == "__main__":
    getModifiedString("kdi39323swe")
    getModifiedString("12345abcdef")
    getModifiedString("12345")
#!/usr/bin/python3

"""Write a Python program that alternates the case of each letter in a given string, 
with the first letter in the string being uppercase.
Original string: Python Exercises
After alternating the case of each letter of the said string: PyThOn ExErCiSeS
Original string: C# is used to develop web apps, desktop apps, mobile apps, games and much more.
After alternating the case of each letter of the said string: C# iS uSeD tO dEvElOp 
WeB aPpS, dEsKtOp ApPs, MoBiLe ApPs, GaMeS aNd MuCh MoRe."""

def altChars(string):
    print("Original string: ",string)
    print("After alternating the case of each letter of the said string: ",end="")
    s = True
    for i in range(len(string)): 
        print(string[i].upper() if s else string[i].lower(),end="")
        if string[i].isalpha(): s = not s
    print()

if __name__ == "__main__":
    altChars("Python Exercises")
    altChars("C# is used to develop web apps, desktop apps, mobile apps, games and much more.")
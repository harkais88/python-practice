#!/usr/bin/python3

"""Write a Python program to create a coded string from a given string, using a specified formula.
Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'
Original string: PHP
Coded string: 969
Original string: JAVASCRIPT
Coded string: J8V81CRI90"""

# def encoder(string):
#     code = {"P": "9", "T": "0", "S": "1", "H": "6", "A": "8"}
#     print("Original string: ",string)
#     print("Coded string: ","".join([i if i not in code.keys() else code[i] for i in list(string)]))

# OR

# def encoder(string):
#    print("Original string: ",string)
#    print("Coded string: ",string.replace("P","9").replace("T","0").replace("S","1").replace("H","6").replace("A","8"))

# OR

def encoder(string: str):
    print("Original string: ",string)
    print("Coded string: ",string.translate(string.maketrans("PTSHA","90168")))

if __name__ == "__main__":
    encoder("PHP")
    encoder("JAVASCRIPT")
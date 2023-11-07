#!/usr/bin/python3

"""Write a Python program to reverse only the vowels of a given string.
Sample Input:
("w3resource")
("Python")
("Perl")
("USA")
Sample Output:
w3resuorce
Python
Perl
ASU"""

def revVowel(string: str):
    vowels = []
    
    for char in string:
        if char.lower() in ["a","e","i","o","u"]:
            vowels += char

    result_string = ""
    for char in string:
        if char.lower() in ["a","e","i","o","u"]:
            result_string += vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string += char

    return result_string    

if __name__ == "__main__":
    print(revVowel("w3resource"))
    print(revVowel("Python"))
    print(revVowel("Perl"))
    print(revVowel("USA"))


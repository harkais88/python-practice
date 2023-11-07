#!/usr/bin/python3

"""Write a Python program to reverse all words of even lengths.
Sample Input:
("The quick brown fox jumps over the lazy dog")
("Python Exercises")
Sample Output:
The quick brown fox jumps revo the yzal dog
nohtyP Exercises"""

def reverseOddWords(string):
    return " ".join([i if len(i) % 2 != 0 else i[::-1] for i in string.split()])

if __name__ == "__main__":
    print(reverseOddWords("The quick brown fox jumps over the lazy dog"))
    print(reverseOddWords("Python Exercises"))
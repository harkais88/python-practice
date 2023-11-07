#!/usr/bin/python3

"""Write a Python program to find the position of the second occurrence of 
a given string in another given string. If there is no such string return -1.
Sample Input:
("The quick brown fox jumps over the lazy dog", "the")
("the quick brown fox jumps over the lazy dog", "the")
Sample Output:
-1
31"""

def getSecondOccurence(string,key):
    return string.find(key, string.find(key)+1)

if __name__ == "__main__":
    print(getSecondOccurence("The quick brown fox jumps over the lazy dog", "the"))
    print(getSecondOccurence("the quick brown fox jumps over the lazy dog", "the"))
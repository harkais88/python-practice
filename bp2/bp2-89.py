#!/usr/bin/python3

"""Write a Python program that accepts two strings and determines whether the letters 
in the second string are present in the first string.
Sample Input:
["python", "ypth"]
["python", "ypths"]
["python", "ypthon"]
["123456", "01234"]
["123456", "1234"]
Sample Output:
True
False
True
False
True"""

def checkIfLettersPresent(str1, str2):
    return all([char in str1 for char in str2])

if __name__ == "__main__":
    print(checkIfLettersPresent("python", "ypth")) 
    print(checkIfLettersPresent("python", "ypths")) 
    print(checkIfLettersPresent("python", "ypthon")) 
    print(checkIfLettersPresent("123456", "01234")) 
    print(checkIfLettersPresent("123456", "1234")) 
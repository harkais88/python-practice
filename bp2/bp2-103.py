#!/usr/bin/python3

"""Write a Python program to create a string with no duplicate consecutive letters from a given string.
Sample Input:
("PPYYYTTHON")
("PPyyythonnn")
("Java")
("PPPHHHPPP")
Sample Output:
PYTHON
Python
Java
PHP"""

def rmvDups(string):
    return string[0] + "".join([string[i] for i in range(1,len(string)) if string[i] != string[i-1]])

if __name__ == "__main__":
    print(rmvDups("PPYYYTTHON"))
    print(rmvDups("PPyyythonnn"))
    print(rmvDups("Java"))
    print(rmvDups("PPPHHHPPP"))
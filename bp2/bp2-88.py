#!/usr/bin/python3

"""Write a Python program to check whether a given employee code is 
exactly 8 digits or 12 digits. Return True if the employee code is valid and False if it's not.
Sample Input:
('12345678')
('1234567j')
('12345678j')
('123456789123')
('123456abcdef')
Sample Output:
True
False
False
True
False"""

def checkEmpCode(string: str) -> bool:
    return True if len(string) in [8,12] and string.isdigit() else False

if __name__ == "__main__":
    print(checkEmpCode('12345678'))
    print(checkEmpCode('1234567j'))
    print(checkEmpCode('12345678j'))
    print(checkEmpCode('123456789123'))
    print(checkEmpCode('123456abcdef'))
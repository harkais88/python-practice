#!/usr/bin/python3

"""Write a Python program to check whether a given integer is a palindrome or not.
Note: An integer is a palindrome when it reads the same backward as forward. 
Negative numbers are not palindromic.
Sample Input:
(100)
(252)
(-838)
Sample Output:
False
True
False"""

def isPalindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(isPalindrome(100))
    print(isPalindrome(252))
    print(isPalindrome(-838))
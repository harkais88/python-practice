#!/usr/bin/python3

"""Write a Python program to find the closest palindrome number to a given integer. 
If there are two palindrome numbers in absolute distance return the smaller number.
Original number: 120
Closest Palindrome number of the said number: 121
Original number: 321
Closest Palindrome number of the said number: 323
Original number: 43
Closest Palindrome number of the said number: 44
Original number: 1234
Closest Palindrome number of the said number: 1221"""

def getPalindrome(num):
    print("Original Number: ",num)
    print("Closest Palindrome number of the said number: ",end = "")
    if str(num) == str(num)[::-1]:
        print(num)
    else:    
        x = num
        y = num
        while True:
            if str(x) == str(x)[::-1]: print(x); break;
            x -= 1;
            if str(y) == str(y)[::-1]: print(y); break;
            y += 1;

if __name__ == "__main__":
    getPalindrome(120)
    getPalindrome(321)
    getPalindrome(43)
    getPalindrome(1234)
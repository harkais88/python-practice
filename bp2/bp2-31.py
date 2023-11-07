#!/usr/bin/python3

"""Write a Python program to reverse the digits of a given number and add them to the original. 
Repeat this procedure until the sum is not a palindrome.
Note: A palindrome is a word, number, or other sequence of characters which reads the same 
backward as forward, such as madam or racecar."""

def isPalindrome(num):
    return str(num)[::-1] == str(num)

def reverse(num):
    return int(str(num)[::-1])

def revSum(num):
    print()
    while True:
        print(" Number now: ",num)
        print()
        revNum = reverse(num)
        print(" Reverse: ",revNum)
        print()
        sum = revNum + num
        print(" Sum: ",sum)
        print()
        if not isPalindrome(sum):
            print(f" {sum} is not a palindrome")
            print()
            break
        else:
            print(f" {sum} is a palindrome")
            print()
            num = sum

if __name__ == "__main__":
    revSum(21)
    revSum(1234)
    revSum(1473)
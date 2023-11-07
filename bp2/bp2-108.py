#!/usr/bin/python3

"""Write a Python program to check whether a given number is oddish or evenish.
A number is called "Oddish" if the sum of all of its digits is odd, 
and a number is called "Evenish" if the sum of all of its digits is even.
Sample Output:
Original Number 120
Check whether the sum of all digits of the said number is odd or even!
Oddish
Original Number 321
Check whether the sum of all digits of the said number is odd or even!
Evenish
Original Number 43
Check whether the sum of all digits of the said number is odd or even!
Oddish
Original Number 4433
Check whether the sum of all digits of the said number is odd or even!
Evenish
Original Number 373
Check whether the sum of all digits of the said number is odd or even!
Oddish"""

def isOddishOrEvenish(num):
    print("Original Number ",num)
    print("Check whether the sum of all digits of the said number is odd or even!")
    print("Oddish" if sum([int(i) for i in list(str(num))]) % 2 != 0 else "Evenish")

if __name__ == "__main__":
    isOddishOrEvenish(120)
    isOddishOrEvenish(321)
    isOddishOrEvenish(43)
    isOddishOrEvenish(4433)
    isOddishOrEvenish(373)
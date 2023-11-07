#!/usr/bin/python3

"""Write a Python program to check whether a given number is a narcissistic number or not.

If you are a reader of Greek mythology, then you are probably familiar with Narcissus. 
He was a hunter of exceptional beauty that he died because he was unable to leave a pool 
after falling in love with his own reflection. That's why I keep myself away from pools these days (kidding).
In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get 
enough of themselves. In particular, they are numbers that are the sum of their digits when 
raised to the power of the number of digits.
For example, 371 is a narcissistic number; it has three digits, and if we cube each 
digits 33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
It has been proven that there are only 88 narcissistic numbers 
(in the decimal system) and that the largest of which is
115,132,219,018,763,992,565,095,597,973,971,522,401
has 39 digits.

Ref.: //https://bit.ly/2qNYxo2
Sample Input:
(153)
(370)
(407)
(409)
(1634)
(8208)
(9474)
(9475)
Sample Output:
True
True
True
False
True
True
True
False"""

from math import pow

def isNarcissit(num):
    return num == sum([pow(int(str(num)[i]),len(str(num))) for i in range(len(str(num)))])

if __name__ == "__main__":
    print(isNarcissit(153))
    print(isNarcissit(370))
    print(isNarcissit(407))
    print(isNarcissit(409))
    print(isNarcissit(1634))
    print(isNarcissit(8208))
    print(isNarcissit(9474))
    print(isNarcissit(9475))
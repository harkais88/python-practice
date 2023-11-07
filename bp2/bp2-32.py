#!/usr/bin/python3

"""Write a Python program to count the number of carry operations for each addition problem.
According to Wikipedia "In elementary arithmetic, a carry is a digit that is transferred 
from one column of digits to another column of more significant digits. It is part of the 
standard algorithm to add numbers together by starting with the rightmost digits and working 
to the left. For example, when 6 and 7 are added to make 13, the "3" is written to the same 
column and the "1" is carried to the left"."""

def carryCount(a,b):
    print(" Number of carries required in the addition of {} and {}: ".format(a,b),end = "")
    count = 0
    carry = 0
    while a != 0 or b != 0:
        sum = (a % 10) + (b % 10) + carry 
        if len(str(sum)) > 1:
            count += 1
            carry = 1
        else:
            carry = 0
        a = a // 10
        b = b // 10
    print(count)
    return count

if __name__ == "__main__":
    carryCount(123,567)
    carryCount(923,77)
    carryCount(6,7)

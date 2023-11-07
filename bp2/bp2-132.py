#!/usr/bin/python3

"""Write a Python program to find all the factors of a given natural number.
Factors:
The factors of a number are the numbers that divide into it exactly. 
The number 12 has six factors:
1, 2, 3, 4, 6 and 12 If 12 is divided by any of the six factors then the answer will be a whole number. 
For example:
12 / 3 = 4
Original Number: 1
Factors of the said number: {1}
Original Number: 12
Factors of the said number: {1, 2, 3, 4, 6, 12}
Original Number: 100
Factors of the said number: {1, 2, 4, 100, 5, 10, 50, 20, 25}"""

from math import sqrt

def getFactors(num):
    print("Original Number: ",num)
    factors = []
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            if num / i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(num // i)
    print("Factors of the said number: ",factors)

# OR

def getFactors(num):
    from functools import reduce
    print("Original Number: ",num)
    print("Factors of the said number: ",set(reduce(list.__add__, 
                                                    ([i, num//i] for i in range(1,int(sqrt(num)+1))
                                                     if num % i == 0))))

if __name__ == "__main__":
    getFactors(1)
    getFactors(12)
    getFactors(100)

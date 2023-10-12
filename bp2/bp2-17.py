#!/usr/bin/python3

"""Write a Python program to get all strobogrammatic numbers that are of length n.
A strobogrammatic number is a number whose numeral is rotationally symmetric, so that 
it appears the same when rotated 180 degrees. In other words, the numeral looks the same 
right-side up and upside down (e.g., 69, 96, 1001).
For example,
Given n = 2, return ["11", "69", "88", "96"].
Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']"""

from num2words import num2words

def getStrob(n,length):
    if n == 0:
        return [""]
    
    if n == 1:
        return ["1","0","8"]
    
    middles = getStrob(n-2,length)
    result = []

    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6") 
        result.append("6" + middle + "9")

    return result

def strobGen(n):
    result = getStrob(n,n)
    return result

def strobPrint(n):
    print(f"\n All {num2words(n)} digit Strobogrammatic numbers: ",strobGen(n))

if __name__ == "__main__":
    strobPrint(1)
    strobPrint(2)
    strobPrint(3)
    strobPrint(4)



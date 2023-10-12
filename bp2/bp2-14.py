#!/usr/bin/python3

"""Write a Python program to add two positive integers without using the '+' operator.
Note: Use bit wise operations to add two numbers."""

def decToBin(num):
    binary = []
    while num != 0:
        binary.append(num % 2)
        num = num // 2
    string = "".join([str(ele) for ele in binary[::-1]])
    return string

def addBin(bin1, bin2):
    result = ""

    carry = 0

    for i in range(max(len(bin1),len(bin2)) - 1, -1, -1):
        r = carry
        r += 1 if bin1[i] == "1" else 0
        r += 1 if bin2[i] == "1" else 0
        result = ("1" if r % 2 == 1 else "0") + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = "1" + result

    return int(result,2)

if __name__ == "__main__":
    num1 = int(input("\n Enter a number: "))
    num2 = int(input("\n Enter another number: "))

    # Getting the binary of both numbers
    bin1 = decToBin(num1)
    bin2 = decToBin(num2)

    # Adding 0 padding for equalling length
    bin1 = bin1.rjust(max(len(bin1),len(bin2)), "0")
    bin2 = bin2.rjust(max(len(bin1),len(bin2)), "0")

    print(f"\n Sum of {num1} and {num2} using bitwise operations: {addBin(bin1,bin2)}")
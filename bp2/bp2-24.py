#!/usr/bin/python3

"""Write a Python program that accepts a positive number and subtracts from it the 
sum of its digits, and so on. Continue this operation until the number is negative"""

def repeatOp(num):
    print("\nFor number = ",num)
    if num < 0:
        print("Needs to be positive")
    else:
        while num > 0:
            print("Current Number: ",num)
            sum_of_digits = sum([int(i) for i in str(num)])
            print("Sum of the digits of {} = {}".format(num, sum_of_digits))
            print("Deducting {} from {}".format(sum_of_digits, num))
            num -= sum_of_digits
            print()
        print("Operation Complete\n")

if __name__ == "__main__":
    repeatOp(9)
    repeatOp(20)
    repeatOp(110)
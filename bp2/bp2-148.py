#!/usr/bin/python3

"""A Python list contains three positive integers. 
Write a Python program to check whether the sum of the digits in each number is equal or not. 
Return true otherwise false.
Sample Data:
([13, 4, 22]) -> True
([-13, 4, 22]) -> False
([45, 63, 90]) -> True"""

def checkEqSumOfDigits(nums):
    print(f"({nums}) -> ",end = "")
    sums = []
    for num in nums:
        f_d = 0
        if num < 0:
            f_d = -int(str(num)[1])
            num = int(str(num)[2:])
        sum = 0
        while num != 0:
            sum += num % 10
            num //= 10
        sum += f_d
        sums.append(sum)
    print(len(set(sums)) == 1)

if __name__ == "__main__":
    checkEqSumOfDigits([13, 4, 22])
    checkEqSumOfDigits([-13, 4, 22])
    checkEqSumOfDigits([45, 63, 90])
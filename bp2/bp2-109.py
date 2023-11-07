#!/usr/bin/python3

"""Write a Python program that takes three integers and checks whether the 
sum of the last digit of the first number and the last digit of the second 
number equals the last digit of the third number.
Sample Input:
(12, 26, 44)
(145, 122, 1010)
(0, 20, 40)
(1, 22, 40)
(145, 129, 104)
Sample Output:
False
False
True
False
False"""

def checkEndDigiSum(n1, n2, n3):
    return int(str(n1)[-1]) + int(str(n2)[-1]) == int(str(n3)[-1])

if __name__ == "__main__":
    print(checkEndDigiSum(12, 26, 44))
    print(checkEndDigiSum(145, 122, 1010))
    print(checkEndDigiSum(0, 20, 40))
    print(checkEndDigiSum(1, 22, 40))
    print(checkEndDigiSum(145, 129, 104))
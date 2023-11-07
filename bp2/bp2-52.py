#!/usr/bin/python3

"""Write a Python program that determines the difference between the largest and smallest 
integers created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
Input:
Input an integer created by 8 numbers from 0 to 9.:
2345
Difference between the largest and the smallest integer from the given integer:
3087"""

if __name__ == "__main__":
    num = list(input("Input an integer created by 8 numbers from 0 to 9.:\n"))

    print("Difference between the largest and the smallest integer from the given integer:")
    print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))
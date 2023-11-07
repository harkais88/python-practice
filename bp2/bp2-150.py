#!/usr/bin/python3

"""Write a Python program that takes a positive integer and 
creates an N x N square filled with the integer N. Display the N x N square.
Sample Data:
(2) -> [[2, 2], [2, 2]]
(5) -> [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
(-6) -> []"""

def matrixGen(num):
    print(f"({num}) -> {[[num for _ in range(num)] for _ in range(num)]}")

if __name__ == "__main__":
    matrixGen(2)
    matrixGen(5)
    matrixGen(-6)
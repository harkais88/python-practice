#!/usr/bin/python3

"""Write a Python program to print a given N by M matrix of numbers 
line by line in forward > backwards > forward >... order.
Input matrix:
[[1, 2, 3,4],
[5, 6, 7, 8],
[0, 6, 2, 8],
[2, 3, 0, 2]]
Output:
1
2
3
4
8
7
6
5
0
6
2
8
2
0
3
2"""

from sys import stdin

def matrixTraverse(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            for ele in matrix[i]:
                print(ele)
        else:
            for ele in matrix[i][::-1]:
                print(ele)

if __name__ == "__main__":
    print("Input row of matrix with elements comma seperated, then press enter to enter new row.")
    print("Press ctrl+z and enter to exit.")
    matrix = [list(map(int,l.split(","))) for l in stdin]
    print("Output:")
    matrixTraverse(matrix)
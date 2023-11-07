#!/usr/bin/python3

"""Write a NumPy program to add elements of a matrix. 
If an element in the matrix is 0, we will not add the element below this element."""

import numpy as np

def sumMatrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] == 0 and i+1 < len(matrix):
                matrix[i+1,j] = 0
            sum += matrix[i,j] 
    return sum

if __name__ == "__main__":
    matrix = np.array([[1, 1, 0, 2],[0, 3, 0, 3], [1, 0, 4, 4]])
    print("Original matrix:\n",matrix)
    print("Sum of elements with given rules: ",sumMatrix(matrix))
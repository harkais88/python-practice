#!/usr/bin/python3

"""Write a NumPy program to add a vector to each row of a given matrix."""

import numpy as np

if __name__ == "__main__":
    vec = np.array([1,2,3,4])
    matrix = np.random.randint(1,10,(4,4))

    print(f"Adding {vec} to each row of the matrix \n{matrix}: ")
    for i in range(matrix.shape[0]): matrix[i,:] += vec;
    print(matrix)
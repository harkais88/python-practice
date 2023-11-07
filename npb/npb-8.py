#!/usr/bin/python3

"""Write a NumPy program to test element-wise for complex numbers, real numbers 
in a given array. Also test if a given number is of a scalar type or not. """

import numpy as np

if __name__ == "__main__":
    arr = np.array([1+2j, 1+0j, 0.5, np.pi])

    print(f"Checking array {arr} element wise for complex numbers: {np.iscomplex(arr)}")
    print(f"Checking array {arr} element wise for real numbers: {np.isreal(arr)}")
    
    num1 = 3.1
    num2 = [3.1]
    print(f"Checking if number {num1} is scalar: {np.isscalar(num1)}")
    print(f"Checking if number {num2} is scalar: {np.isscalar(num2)}")
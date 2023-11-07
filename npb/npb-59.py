#!/usr/bin/python3

"""Write a NumPy program to multiply two given arrays of the same size element-by-element."""

import numpy as np

if __name__ == "__main__":
    arr1 = np.random.randint(1,10,(4,4))
    arr2 = np.random.randint(1,10,(4,4))
    print(f"Arrays:\n{arr1}\n{arr2}")
    print("Multiplying the arrays element-by-element:\n",np.multiply(arr1,arr2))
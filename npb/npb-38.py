#!/usr/bin/python3

"""Write a NumPy program to convert a given array into bytes, and load it as an array."""

import numpy as np

if __name__ == "__main__":
    arr = np.arange(1,11)
    print("Original array: ",arr,"\nConverting array to bytes")
    arr_bytes = arr.tobytes()
    print("In bytes form: ",arr_bytes)
    print("Converting back to array")
    arr_bytes = np.frombuffer(arr,dtype=arr.dtype) 
    print("Array found: ",arr_bytes)
    print("Are they equal? ",np.array_equal(arr,arr_bytes))

#!/usr/bin/python3

"""Write a NumPy program to convert numpy dtypes to native Python types"""

import numpy as np

if __name__ == "__main__":
    arr = np.arange(10)
    print(f"Numpy array {arr} data type: ",type(arr))
    print(f"Converting array {arr} to list: ",arr.tolist())
    print(f"Converting array {arr} to numpy.float32: ",np.float32(arr))
    print(f"Data type of the items in {np.float32(arr)}: ",type(np.float32(arr)[0].item()))
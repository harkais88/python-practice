#!/usr/bin/python3

"""Write a Python program to get the execution time of a Python method."""

import time
import numpy as np

def sum(*args):
    sum = 0
    for argv in args:
        sum += argv
    return sum

if __name__ == "__main__":
    start = time.time_ns()
    print(sum(1,2,3,4,5,6,7,8,9,0,10,12,2,123,23,124,1342,124,124,124,124,4,14,14,141,41,241,42,14,14,14,
              1,412,41,41,414,1,424,124,12,41,41,24,124,12,4,142,12,41,42,214,1,41,24))
    end = time.time_ns()
    print("\n Execution time: {}ns".format(end-start))
#!/usr/bin/python3

"""Write a Python program to sum the first n positive integers."""

import time

if __name__ == "__main__":
    n = int(input("\n Enter the number of integers: "))

    start = time.time_ns()    
    original = n
    sum = 0

    while n >= 1:
        sum += n
        n -= 1

    end = time.time_ns()

    print("\n Sum of first {} positive integers: {} \n Execution Time: {}ns".format(original,sum,end-start))

    #Although, there is a much more better way, which at this time, I forgot :(
    
    start = time.time_ns()
    sum = (original * (original+1))//2
    end = time.time_ns()
    
    print("\n Sum of first {} positive integers: {} \n Execution Time: {}ns".format(original,sum,end-start))
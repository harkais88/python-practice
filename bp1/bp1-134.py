#!/usr/bin/python3

"""Write a Python program to calculate the time runs (difference between start and current time) of a program. """

from random import randint
import time

def add(*argv):
    sum = 0
    for arg in argv:
        sum += arg
    return sum

if __name__ == "__main__":
    #We can do it using the time.time() function
    start = time.time()
    
    nums = [randint(1,1000) for _ in range(10)]

    a,b,c,d,e,f,g,h,i,j = nums
    print(" Sum: ",add(a,b,c,d,e,f,g,h,i,j))

    end = time.time()

    print("\n Time Run: ",end-start)

    #Or we could use the default_timer function from timeit for a more accurate timing
    from timeit import default_timer

    start = default_timer()

    nums = [randint(1,1000) for _ in range(10)]

    a,b,c,d,e,f,g,h,i,j = nums
    print(" Sum: ",add(a,b,c,d,e,f,g,h,i,j))

    print(" Time run: ", default_timer() - start)

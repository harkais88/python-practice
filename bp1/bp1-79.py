"""Write a Python program to get the size of an object in bytes"""

import sys

def size(obj):
    print("\n Size of {}: {}".format(obj,sys.getsizeof(obj)))

if __name__ == "__main__":
    x = 1
    y = 1.0
    z1 = ""
    z2 = " "
    z3 = "A"
    A = []
    B = ()
    C = {}
    size(x)
    size(y)
    size(z1)
    size(z2)
    size(z3)
    size(A)
    size(B)
    size(C)

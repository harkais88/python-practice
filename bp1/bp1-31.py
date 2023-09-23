"""Write a Python program that computes the greatest common divisor (GCD) of two positive integers."""

import sys

#One way to do it
def min(a,b):
    return a if a<b else b

if __name__ == "__main__":
    n1 = int(input("\n Enter a number: "))
    n2 = int(input("\n Enter another number: "))

    if n1 % n2 == 0:
        print("\n GCD of {} and {}: {}".format(n1,n2,n2))
        sys.exit()
    if n2 % n1 == 0:
        print("\n GCD of {} and {}: {}".format(n1,n2,n1))
        sys.exit()

    GCD = min(n1,n2)/2

    while n1 % GCD != 0 or n2 % GCD != 0:
        GCD -= 1

    print("\n GCD of {} and {}: {}".format(n1,n2,GCD)) 

#Another way to do it

# def GCD(a,b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a

#     if a == b:
#         return a

#     if a>b:
#         return GCD(a-b,b)
#     return GCD(a,b-a)

# if __name__ == "__main__":
#     n1 = int(input("\n Enter a number: "))
#     n2 = int(input("\n Enter another number: "))

#     print("\n GCD of {} and {}: {}".format(n1,n2,GCD(n1,n2)))
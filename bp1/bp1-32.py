#!/usr/bin/python3

"""Write a Python program to find the least common multiple (LCM) of two positive integers."""

# #One way to do it
# def max(a,b):
#     return a if a>b else b

# if __name__ == "__main__":
#     n1 = int(input("\n Enter a number: "))
#     n2 = int(input("\n Enter another number: "))

#     LCM = max(n1,n2)

#     while (LCM % n1 != 0 or LCM % n2 != 0) and LCM <= n1 * n2:
#         LCM += max(n1,n2)

#     print("\n LCM of {} and {}: {}".format(n1,n2,LCM))

#Another way, and it is probably way more efficient
def GCD(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        return GCD(a-b,b)
    return GCD(a,b-a)

#Based on the formula that HCF(a,b) * LCM(a,b) = a*b for any a,b belonging to the positive number set
def LCM(a,b):
    return (a*b) // GCD(a,b)

if __name__ == "__main__":
    n1 = int(input("\n Enter a number: "))
    n2 = int(input("\n Enter another number: "))

    print("\n LCM of {} and {}: {}".format(n1,n2,LCM(n1,n2)))

    
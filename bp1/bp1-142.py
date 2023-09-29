#!/usr/bin/python3

"""Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04 """

if __name__ == "__main__":
    # We could convert a decimal to it's equivalent hexadecimal by dividing it by 13 and noting the remainders until q=0, and then reversing the remainders
    # Ex -  30/16 => q=1, r=14 = e (in hex, A = 10, B = 11, C = 12, D = 13, E = 14, F = 15)
    #       1/16 => q=0, r=1
    # So, 30 in hexadecimal = 1e

    # In python, we can simply use the inbuilt hex() function to convert a decimal to a hexadecimal
    n1,n2 = 30,4

    print("{} and {} in hex form: {},{}".format(n1,n2,hex(n1),hex(n2)))
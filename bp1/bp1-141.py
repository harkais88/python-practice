#!/usr/bin/python3

"""Write a Python program to convert an integer to binary that keeps leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100"""

if __name__ == "__main__":
    x = 12

    # Normally, you could convert an integer to it's equivalent binary by dividing it by 2 and noting the remainders until q=0, and then reversing it
    # Ex-   12/2 => q=6, r=0
    #       6/2 => q=3, r=0
    #       3/2 => q=1, r=1
    #       1/2 => q=0, r=1  
    # Therefore, 12 in binary = 1100

    # In Python, you can simply use the inbuilt format function for this purpose

    # Use format() to convert an integer to binary with leading zeros. Call format(num, name) with name as "0nb" 
    # to convert an integer num to a binary string with leading zeros up to length n 
    print(format(x, "08b"))
    print(format(x, "010b"))
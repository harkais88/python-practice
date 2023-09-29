#!/usr/bin/python3

"""Write a Python program to check whether an integer fits in 64 bits."""

if __name__ == "__main__":
    num_1ist = [2**63, 18446744073709551616, 17446744073309551616, 19946744073709551616, -2**63]

    for num in num_1ist:
        if num.bit_length() <= 64:
            print(num, "fits in under or equal to 64 bits")
        else:
            print(num, "does not fit in under or equal to 64 bits")
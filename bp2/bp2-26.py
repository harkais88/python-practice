#!/usr/bin/python3

"""Write a Python program to find the digits that are missing from a given mobile number."""

if __name__ == "__main__":
    phone = set([int(i) for i in input("\n Enter a phone number: ")])

    # Symmetric Difference is only available for set data types
    print("\n All missing digits from this phone number: ",phone.symmetric_difference([0,1,2,3,4,5,6,7,8,9]))
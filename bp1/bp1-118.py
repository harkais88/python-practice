#!/usr/bin/python3

"""Write a Python program to prove that two string variables of the same value point to the same memory location."""

if __name__ == "__main__":
    string1 = "Arka"
    string2 = "Arka"

    # # One way to get address of variables
    address1 = id(string1)
    address2 = id(string2)

    # Another way to do it
    # from ctypes import addressof, c_wchar_p
    # address1 = addressof(c_wchar_p(string1))
    # address2 = addressof(c_wchar_p(string2))

    # # Opitonally, You could represent the addresses in hex form
    # address1 = hex(address1)
    # address2 = hex(address2)

    print("Address of string1: ",address1)
    print("Address of string2: ",address2)

    print("Are the addresses equal? ",address1 == address2) # Should print True
    if id(string1) == id(string2): 
        print(u"This proves that two strings of equal value point to the same memory location \U0001F62F")
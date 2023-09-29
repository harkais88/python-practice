#!/usr/bin/python3

"""Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS."""

import platform, struct

if __name__ == "__main__":
    #struct.calcsize("P") returns the size of the C char * in bytes. We then convert it to bits as 1 byte = 8 bits
    print(struct.calcsize("P")*8) 
    print(platform.architecture()[0])
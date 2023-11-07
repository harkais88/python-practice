#!/usr/bin/python3

"""Write a Python program to reverse the binary representation of a given number and 
convert the reversed binary number into an integer.
Original number: 13
Reverse the binary representation of the said integer and convert it into an integer: 11
Original number: 145
Reverse the binary representation of the said integer and convert it into an integer: 137
Original number: 1342
Reverse the binary representation of the said integer and convert it into an integer: 997"""

def revBin(num):
    print("Original number: ",num)
    print("Reverse the binary representation of the said integer and convert it into an integer: ",end="")
    print(int(bin(num).replace("0b","")[::-1],base=2))

if __name__ == "__main__":
    revBin(13)
    revBin(145)
    revBin(1342)
#!/usr/bin/python3

"""Write a Python program to find the highest and lowest number from a given string of space-separated integers.
Original string: 1 4 5 77 9 0
Highest and lowest number of the said string: (77, 0)
Original string: -1 -4 -5 -77 -9 0
Highest and lowest number of the said string: (0, -77)
Original string: 0 0
Highest and lowest number of the said string: (0, 0)"""

def highAndLow(string):
    print("Original string: ",string)
    print("Highest and lowest number of the said string: ",end = "")
    # print(f"({max(string.split())},{min(string.split())})")
    result = sorted(map(int,string.split()))
    print(f"({result[-1]},{result[0]})")

if __name__ == "__main__":
    highAndLow("1 4 5 77 9 0")
    highAndLow("-1 -4 -5 -77 -9 0")
    highAndLow("0 0")
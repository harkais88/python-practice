#!/usr/bin/python3

"""Write a Python program to find the longest common ending between two given strings.
Original strings: running ruminating
Common ending between said two strings: ing
Original strings: thisisatest testing123testing
Common ending between said two strings:"""

def getCommonEnds(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1] == str1[-1]:
            return str2[i:]
    return ""

if __name__ == "__main__":
    print("Original string: running ruminating")
    print("Common ending between said two strings: ",getCommonEnds("running", "ruminating"))
    print("Original string: thisisatest testing123testing")
    print("Common ending between said two strings: ",getCommonEnds("thisisatest", "testing123testing"))
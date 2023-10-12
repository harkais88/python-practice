#!/usr/bin/python3

"""Write a Python program that finds the value of n when n number of degrees of number 2 
are written sequentially on a line without spaces between them.

Example - '248163264' => n = 6 """

def isdegOf2(num):
    if num == 1:
        return False
    while num != 1:
        if not (num / 2).is_integer():
            return False
        num = num / 2
    return True

if __name__ == "__main__":
    str = '2481632'
    n = 0
    temp = ""

    for i in range(len(str)):
        temp += str[i]
        if isdegOf2(int(temp)):
            n += 1
            temp = ""
        
    print(n)

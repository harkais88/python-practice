#!/usr/bin/python3

"""Write a Python program to count the number of arguments in a given function.
Sample Input:
()
(1)
(1, 2)
(1, 2, 3)
(1, 2, 3, 4)
[1, 2, 3, 4]
Sample Output:
0
1
2
3
4
1"""

def countArgs(*args):
    return len(args)

if __name__ == "__main__":
    print(countArgs())
    print(countArgs(1))
    print(countArgs(1, 2))
    print(countArgs(1, 2, 3))
    print(countArgs(1, 2, 3, 4))
    print(countArgs([1, 2, 3, 4]))
    
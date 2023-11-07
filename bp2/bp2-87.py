#!/usr/bin/python3

"""Write a Python program to count the number of equal numbers from three given integers.
Sample Input:
(1, 1, 1)
(1, 2, 2)
(-1, -2, -3)
(-1, -1, -1)
Sample Output:
3
2
0
3"""

def noOfEquals(n1,n2,n3):
    if len(set([n1,n2,n3])) == 3: # Means no equals were found
        return 0
    else:
        return 4 - len(set([n1,n2,n3])) 

if __name__ == "__main__":
    print(noOfEquals(1,1,1))
    print(noOfEquals(1,2,2))
    print(noOfEquals(-1,-2,-3))
    print(noOfEquals(-1,-1,-1))
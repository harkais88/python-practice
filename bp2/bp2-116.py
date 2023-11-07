#!/usr/bin/python3

"""Write a Python program to generate and print a list of numbers from 1 to 10.
Sample Input:
range(1,10)
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']"""

if __name__ == "__main__":
    li = [i for i in range(1,10)]
    print(li)
    print(list(map(str,li)))
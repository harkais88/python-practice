#!/usr/bin/python3

"""Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.
Note: Use random.sample() to generate a list of random values.
Sample Input:
(1,100)
Sample Output:
[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]"""

from random import sample

if __name__ == "__main__":
    print(sample([i for i in range(2,101,2)], k = 10))
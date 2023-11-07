#!/usr/bin/python3

"""Write a Python program to compute the digit distance between two integers.
The digit distance between two numbers is the sum of the absolute values of the difference of the 
digits of the numbers.
For example, the distance between 3 and -3 on the number line given by the |3 - (-3) | = |3 + 3 | = 6 units
Digit distance of 123 and 256 is 7
Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7
Sample Input:
(123, 256)
(23, 56)
(1, 2)
(24232, 45645)
Sample Output:
7
6
1
11"""

def digitDist(a, b):
    return sum([abs(int(i) - int(j)) for i,j in zip(str(a),str(b))])

if __name__ == "__main__":
    print(digitDist(123, 256))
    print(digitDist(23, 56))
    print(digitDist(1, 2))
    print(digitDist(24232, 45645))

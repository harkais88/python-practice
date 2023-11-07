#!/usr/bin/python3

"""Arrange integers (between 0 and 99, inclusive) in a diamond, like the following:

        8
       4,9
      9,2,1
     3,8,5,5
    5,6,3,7,6
     3,8,5,5
      9,2,1
       4,9
        8
        
Write a program that reads data that represents a diamond like this, and 
outputs the maximum value of the sum of integers that passes through when 
starting at the top and proceeding to the bottom according to the rule that 
AT EVERY STEP, YOU CAN GO DIAGONALLY TO THE LEFT OR THE RIGHT

For example, here the maximum will be 64 (8 + 4 + 9 + 8 + 6 + 8 + 9 + 4 + 8)
    
Input:
A sequence of integers separated by commas is given to the diamond.
Each line does not contain white space.
Input the numbers (ctrl+z and enter to exit in Windows, ctrl+d and enter to exit in Linux)
7
3,8
8,1,0
2,7,4,4
4,5,2,6,5
2,7,4,4
8,1,0
3,8
7
Output:
Maximum value of the sum of integers passing according to the rule on one line.
55"""

from sys import stdin

if __name__ == "__main__":
    diamond = [list(map(int, l.split(","))) for l in stdin]
    mvv = diamond[0]

    for i in range(1,(len(diamond)+1)//2):
        print("Iteration ",i)
        rvv = [0] * (i+1)
        print(f"rvv = {rvv}, mvv = {mvv}")
        for j in range(i):
            rvv[j] = max(rvv[j], mvv[j] + diamond[i][j])
            rvv[j+1] = max(rvv[j+1], mvv[j] + diamond[i][j+1])
        print(f"rvv now = {rvv}")
        mvv = rvv

    for i in range((len(diamond)+1)//2, len(diamond)):
        print("Iteration ",i)
        rvv = [0] * (len(mvv) - 1)
        print(f"rvv = {rvv}, mvv = {mvv}")
        for j in range(len(rvv)):
            rvv[j] = max(mvv[j], mvv[j+1]) + diamond[i][j]
        print(f"rvv now = {rvv}")
        mvv = rvv

    print("Maximum value of the sum of integers passing according to the rule on one line.")
    print(mvv[0])
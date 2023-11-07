#!/usr/bin/python3

"""There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. 
Blue represents the sea, and green represents the land. When two green squares are in contact with 
the top and bottom, or right and left, they are said to be ground. The area created by only one green 
square is called "island". For example, there are five islands in the figure below.
Write a Python program to read the mass data and find the number of islands.
Input:
Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros
1100000111
1000000111
0000000111
0010001000
0000011100
0000111110
0001111111
1000111110
1100011100
1110001000
Number of islands:
5"""

def islandDetect(world):
    num_of_islands = 0
    for area in world:
        for square_index in range(len(area)):
            if area[square_index] == "1":
                if square_index == 0 and area[square_index+1] == "0":
                    num_of_islands += 1
                elif square_index == len(area)-1 and area[square_index-1] == "0":
                    num_of_islands += 1
                elif area[square_index-1] == "0" and area[square_index+1] == "0":
                    num_of_islands += 1
    return num_of_islands

if __name__ == "__main__":
    print("Input 10 rows of 10 numbers representing green squares (island) as 1s and blue squares (sea) as 0s")
    world = [list(input()) for _ in range(10)]
    print(f"Number of islands:\n{islandDetect(world)}")
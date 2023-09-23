"""Write a Python program to create a histogram pattern from a given list of integers.
Sample Input: 2,3,6,5
Sample Output:
    @@
    @@@
    @@@@@@
    @@@@@
"""

if __name__ == "__main__":
    pattern = [int(i) for i in input("\n Enter a list of integers: ").split(",")]

    for i in range(len(pattern)):
        print(end=" ")
        for j in range(pattern[i]):
            print("@",end="")
        print()


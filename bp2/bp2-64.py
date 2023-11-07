#!/usr/bin/python3

"""Write a Python program that adds up the columns and rows of the given table as shown in the specified figure.
Input number of rows/columns (0 to exit)
4
Input cell value:
25 69 51 26
68 35 29 54
54 57 45 63
61 68 47 59
Result:
25 69 51 26 171
68 35 29 54 186
54 57 45 63 219
61 68 47 59 235
208 229 172 202 811
Input number of rows/columns (0 to exit)"""

if __name__ == "__main__":
    n = int(input("Input number of rows/columns:\n"))
    print("Input cell value:")
    table = [[int(i) for i in input().split()] for _ in range(n)]

    # Row sums
    for i in range(len(table)):
        table[i].append(sum(table[i]))

    # Column sums
    col_sum = []
    for i in range(len(table)+1):
        sum = 0
        for j in range(len(table)):
            sum += table[j][i]
        col_sum.append(sum)
    table.append(col_sum)

    print("Result:")
    for i in range(len(table)):
        for j in range(len(table)):
            print(f"{table[i][j]} ",end="")
        print()
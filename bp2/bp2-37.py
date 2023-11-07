#!/usr/bin/python3

"""Write a Python program to compute the amount of debt in n months. 
Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.
Input:
An integer n (0 <= n <= 100)
Input number of months: 7
Amount of debt: $144000"""

def debtCal(months):
    debt = 100000
    if months > 0:
        for i in range(months):
            debt += int(0.05 * debt)
            if debt % 1000 != 0:
                debt = int(str(debt)[:len(str(debt))-3] + "000") + 1000
    return debt

if __name__ == "__main__":
    months = int(input("\n Input number of months: "))
    print(" Amount of debt: $",debtCal(months))
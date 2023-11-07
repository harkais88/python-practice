#!/usr/bin/python3

"""Write a Python program to check whether a given month and year contains a Monday 13th.
Month No.: 11 Year: 2022
Check whether the said month and year contains a Monday 13th.: False
Month No.: 6 Year: 2022
Check whether the said month and year contains a Monday 13th.: True"""

import datetime

def isDate13Monday(m,y):
    print(f"Month No.: {m} Year: {y}")
    print("Check whether the said month and year contains a Monday 13th.: ",end="")
    print(datetime.date(year = y, month=m, day=13).isoweekday() == 1)

if __name__ == "__main__":
    isDate13Monday(11,2022)
    isDate13Monday(6,2022)
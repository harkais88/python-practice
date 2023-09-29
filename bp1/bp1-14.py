#!/usr/bin/python3

"""Write a Python program to calculate the number of 
days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

import datetime

if __name__ == "__main__":
    date1 = datetime.date(2010,7,2)
    date2 = datetime.date(2014,7,11)

    print("\n ",date2-date1)
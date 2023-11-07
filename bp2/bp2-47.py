#!/usr/bin/python3

"""Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) 
and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
Input:
Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
Input month and date (separated by a single space):
5 15
Name of the date: Sunday"""

from datetime import date 

if __name__ == "__main__":
    year = 2016
    weekdays = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 
                4: "Thursday", 5: "Friday", 6: "Saturday", 
                7: "Sunday"}

    print("Two integers m and d separated by a single space in a line, m ,d represent the month and the day.")
    m,d = [int(i) for i in input("Input month and date (separated by a single space):\n").split()]
    given_date = date(year,m,d)
    print("Name of the date: ",weekdays[given_date.isoweekday()])

    
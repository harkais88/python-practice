"""Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module."""

import calendar

if __name__ == "__main__":
    year = int(input("\n Enter the year: "))
    month = input("\n Enter the month: ")
    month = list(calendar.month_abbr).index(month)

    cal = calendar.month(year,month)
    print()
    print(cal)



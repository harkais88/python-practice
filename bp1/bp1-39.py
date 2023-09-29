#!/usr/bin/python3

"""Write a Python program to compute the future value of a specified principal amount, rate of interest, 
and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79"""

#We know that the formula for compound interest is Amount = Principal * ((1 + rate/n))^n*time
#Here, n means the number of times it is applied in a year. For our purpose, let us 
#just consider the default that is n=100

if __name__ == "__main__":
    principal = float(input("\n Enter a principal amount: "))
    rate = float(input("\n Enter the rate of interest: "))
    years = float(input("\n Enter the number of years: "))

    print("\n The principal amount {}, at the rate of {}%, will increase to {} in {} years".format(
       principal, rate, principal * ((1+(rate/100))**years), years 
    ))
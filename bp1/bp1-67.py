#!/usr/bin/python3

"""Write a Python program to convert pressure in kilopascals to pounds per square inch, 
a millimeter of mercury (mmHg) and atmosphere pressure."""

if __name__ == "__main__":
    kpa = float(input("Input pressure in in kilopascals: "))
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325

    print("\n Pressure in pounds per square inch: {:.2f} PSI\
           \n Pressure in millimeter of mercury: {:.2f} mmHG \
           \n Pressure in atmosphere pressure: {:.2f} atm".format(psi,mmhg,atm))
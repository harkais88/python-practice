"""Write a Python program to convert the distance (in feet) to inches, yards, and miles."""

if __name__ == "__main__":
    #1 Feet = 12 inches
    #1 Feet = 1/3 yards
    #1 Feet = 1/5280 miles

    feet = float(input("\n Enter the length in feet: "))

    print("\n Length in Inches: {} \
          \n Length in Yards: {} \
          \n Length in Miles: {}".format(feet*12, feet/3, feet/5280))
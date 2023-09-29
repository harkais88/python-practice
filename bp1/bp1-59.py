#!/usr/bin/python3

"""Write a Python program to convert height (in feet and inches) to centimeters."""

if __name__ == "__main__":
    #1 Feet = 12 inches
    #1 inch = 2.54 cm

    #Height should be a tuple of feet and inches
    height = [float(i) for i in input("\n Enter the height in feet,inches: ").split(",")]

    height_in_cms = round(2.54*(height[0]*12 + height[1]))

    print("\n Height in cms: ",height_in_cms,"cm")
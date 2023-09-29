#!/usr/bin/python3

"""Write a Python program to calculate the body mass index."""

if __name__ == "__main__":
    weight = float(input("\n Enter your weight in kgs: "))
    height = float(input("\n Enter your height in meters: "))

    print("\n BMI according to Metric System: %.2f"% (weight/(height**2)))
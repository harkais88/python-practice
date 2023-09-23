"""Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20."""

if __name__ == "__main__":
    n1,n2 = [int(i) for i in input("\n Enter 2 numbers seperated by commas: ").split(",")]

    print(" ",20 if n1+n2 >= 15 and n1+n2 <= 20 else n1+n2)
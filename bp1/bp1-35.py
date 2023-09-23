"""Write a Python program that returns true if the two given integer values are equal or 
their sum or difference is 5."""

if __name__ == "__main__":
    n1,n2 = [int(i) for i in input("\n Enter 2 numbers seperated by commas: ").split(",")]

    print(True if n1 == n2 or abs(n1 - n2) == 5 or n1+n2 == 5 else False)
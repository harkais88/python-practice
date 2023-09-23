"""Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""

from math import pow

if __name__ == "__main__":
    x = int(input("\n Enter a number: "))
    y = int(input("\n Enter another number: "))

    print("\n Output: ",(x+y)**2)
    print("\n Output using pow function: ",pow((x+y),2))
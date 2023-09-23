"""Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum."""

if __name__ == "__main__":
    # n1 = int(input("\n Enter a number: "))
    # n2 = int(input("\n Enter another number: "))
    # n3 = int(input("\n Enter yet another number: "))

    [n1,n2,n3] = [int(i) for i in input("\n Enter 3 numbers: ").split(",")]

    print(3*(n1 + n2 + n3) if n1 == n2 == n3 else n1 + n2 + n3)

"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero."""

if __name__ == "__main__":
    [n1,n2,n3] = [int(i) for i in input("\n Enter three integers, seperated by commas: ").split(",")]

    sum = 0
    if n1 != n2 and n1 != n3 and n2 != n3:
        sum = n1 + n2 + n3

    print("\n Sum: ",sum)
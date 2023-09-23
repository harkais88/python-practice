"""Write a Python program to calculate sum of digits of a number."""

if __name__ == "__main__":
    n = int(input("\n Enter a number: "))

    sum = 0
    while n != 0:
        sum += (n % 10)
        n = n // 10

    print("\n Sum of the digits: ",sum)
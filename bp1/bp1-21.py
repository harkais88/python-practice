"""Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user."""

if __name__ == "__main__":
    n = int(input("\n Enter a number: "))

    print(" It is even" if n % 2 == 0 else " It is odd")
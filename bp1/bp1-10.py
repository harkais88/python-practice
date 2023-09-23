"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615"""

if __name__ == "__main__":
    # The Arithmetic Way
    # n = abs(int(input("\n Enter an integer (-ve will be considered +ve): ")))

    # print("\n Result : ", n + (n*10 + n) + (n*100 + n*10 + n))

    # The String Way :|
    n = abs(int(input("\n Enter the integer:")))

    # n1 = int("{}".format(n))
    # n2 = int("{}{}".format(n,n))
    # n3 = int("{}{}{}".format(n,n,n))

    n1 = int(f"{n}")
    n2 = int(f"{n}{n}")
    n3 = int(f"{n}{n}{n}")

    print(" Result: ",n1+n2+n3)
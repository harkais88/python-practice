"""Write a Python program to test whether all numbers in a list are greater than a certain number."""

from random import randint

def chck(list,threshold):
    for ele in list:
        if ele < threshold:
            return False
    return True

if __name__ == "__main__":
    n = int(input("\n Enter a max number, a list of 1000 numbers <= the number will be generated: "))

    list = [randint(1,n) for _ in range(1000)]

    threshold = int(input("\n Enter the threshold: "))

    #We could do it in the following way
    print("\n Are all the numbers in the list greater than the threshold? ",chck(list,threshold))

    #Or we could use the inbuilt all function
    print("\n Are all the numbers in the list greater than the threshold? ",all(ele > threshold for ele in list))
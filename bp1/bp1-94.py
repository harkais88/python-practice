"""Write a Python program to convert the bytes in a given string to a list of integers."""

from sys import getsizeof

if __name__ == "__main__":
    string = input("\n Enter a string: ")
    
    size = getsizeof(string)

    print("\n Size of {}: {} bytes".format(string, size))

    list = []

    while size != 0:
        list.append(size%10)
        size = size//10

    list.reverse()

    print(" In the form of a list: ",list)
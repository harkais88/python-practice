#!/usr/bin/python3

"""Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

def chck(list,n):
    if n in list:
        return True
    return False

if __name__ == "__main__":
    # list1 = input("\n Enter a list of numbers seperated by commas: ").split(",")
    # n1 = input("\n Enter the value you want to search for: ")

    list = [1,5,8,3]
    n1 = 3
    n2 = -1

    print("{} -> {} : {}".format(n1,list,chck(list,n1)))
    print("{} -> {} : {}".format(n2,list,chck(list,n2)))

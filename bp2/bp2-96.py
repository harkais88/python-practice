#!/usr/bin/python3

"""Write a Python program that checks whether every even index contains an even 
number and every odd index contains an odd number of a given list.
Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 3]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
True
Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
False
Original list of numbers: [4,1,2]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
True"""

def checkIndexType(list):
    print("Original list of numbers: ",list)
    print("Check whether every even index contains an even number and every")
    print("odd index contains odd number of a given list")
    print(all([True if (i%2 == list[i]%2) else False for i in range(len(list))]))

if __name__ == "__main__":
    checkIndexType([2, 1, 4, 3, 6, 7, 6, 3])
    checkIndexType([2, 1, 4, 3, 6, 7, 6, 4])
    checkIndexType([4,1,2])
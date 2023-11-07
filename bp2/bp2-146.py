#!/usr/bin/python3

"""Write a Python program to find the largest and smallest digits of a given number.
Original Number: 9387422
Largest Digit of the said number: 9
Smallest Digit of the said number: 2
Original Number: 500
Largest Digit of the said number: 5
Smallest Digit of the said number: 0
Original Number: 231548
Largest Digit of the said number: 8
Smallest Digit of the said number: 1"""

def getLargestAndSmallest(num):
    print("Original Number: ",num)
    print("Largest Digit of the said number: ",max(map(int,list(str(num)))))
    print("Smallest Digit of the said number: ",min(map(int,list(str(num)))))

if __name__ == "__main__":
    getLargestAndSmallest(9387422)
    getLargestAndSmallest(500)
    getLargestAndSmallest(231548)
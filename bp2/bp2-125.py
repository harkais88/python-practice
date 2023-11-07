#!/usr/bin/python3

"""Write a Python program to check if a given string contains two similar consecutive letters.
Original string: PHP
Check for consecutive similar letters! False
Original string: PHHP
Check for consecutive similar letters! True
Original string: PHPP
Check for consecutive similar letters! True"""

def checkForConsecutives(string):
    print("Original string: ",string)
    print("Check for consecutive similar letters! ",any(string[i] == string[i-1] for i in range(1,len(string))))

if __name__ == "__main__":
    checkForConsecutives("PHP")
    checkForConsecutives("PHHP")
    checkForConsecutives("PHPP")


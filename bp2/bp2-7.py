#!/usr/bin/python3

"""Write a Python program to count the number of each character in a text file."""

if __name__ == "__main__":
    log = {}
    file = open(__file__,"r")
    
    while True:
        char = file.read(1)

        if not char:
            break

        if char not in log.keys():
            log[char] = 1
        else:
            log[char] += 1

    print(" Getting the number of each character in this file: ",log)

    file.close()
#!/usr/bin/python3

"""Write a Python program to convert all units of time into seconds."""

from math import pow

if __name__ == "__main__":
    time = float(input("\n Enter the time: "))

    while True:
        unit = input("\n Enter the unit given (ms, mcs, ns, ps, fs, days, hours, minutes): ").lower()

        print("Time in seconds: ",end = "")
        match unit:
            case "ms": 
                print(time/pow(10,3))
                break
            case "mcs": 
                print(time/pow(10,6))
                break
            case "ns": 
                print(time/pow(10,9))
                break
            case "ps": 
                print(time/pow(10,12))
                break
            case "fs": 
                print(time/pow(10,15))
                break
            case "days":
                print(time*24*60*60)
                break
            case "hours":
                print(time*60*60)
                break
            case "minutes":
                print(time*60)
                break
            case _:
                print("\n Invalid time unit")
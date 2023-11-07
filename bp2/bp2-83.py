#!/usr/bin/python3

"""Write a Python program to calculate the median from a list of numbers.
Sample Input:
[1,2,3,4,5]
[1,2,3,4,5,6]
[6,1,2,4,5,3]
[1.0,2.11,3.3,4.2,5.22,6.55]
[1.0,2.11,3.3,4.2,5.22]
[2.0,12.11,22.3,24.12,55.22]
Sample Output:
3
3.5
3.5
3.75
3.3
22.3"""

def median(list):
    return sorted(list)[(len(list)//2)] if len(list) % 2 != 0 \
            else (sorted(list)[(len(list)//2)-1] + sorted(list)[(len(list)//2)]) / 2

if __name__ == "__main__":
    print(median([1,2,3,4,5]))
    print(median([1,2,3,4,5,6]))
    print(median([6,1,2,4,5,3]))
    print(median([1.0,2.11,3.3,4.2,5.22,6.55]))
    print(median([1.0,2.11,3.3,4.2,5.22]))
    print(median([2.0,12.11,22.3,24.12,55.22]))
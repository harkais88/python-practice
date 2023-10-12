#!/usr/bin/python3

"""Write a Python program to find the median among three given numbers."""

# The Python Way, lol
# def getMedian(n1,n2,n3):
#     return sorted([n1,n2,n3])[1]

def getMedian(n1,n2,n3):
    if n1 < n2 and n2 < n3:
        return n2
    
    elif n1 < n3 and n3 < n2:
        return n3

    elif n2 < n1 and n1 < n3:
        return n1

    elif n2 < n3 and n3 < n1:
        return n3
    
    elif n3 < n1 and n1 < n2:
        return n1

    elif n3 < n2 and n2 < n1:
        return n2

if __name__ == "__main__":
    print(getMedian(1,9,2))
    print(getMedian(25,15,35))
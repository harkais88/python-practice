#!/usr/bin/python3

"""Write a Python program to find the type of the progression (arithmetic progression / geometric progression) 
and the next successive member of a sequence.

According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers 
such that the difference of any two successive members of the sequence is a constant. 
For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2. 
For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.

On the other hand, a geometric progression (GP) is a sequence of numbers where each term after 
the first is found by multiplying the previous one by a fixed non-zero number called the common ratio. 
For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. 
For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer."""

def idenProg(seq: list):
    # Checking if sequence is an AP
    if APCheck(seq):
        diff = seq[-1] - seq[-2]
        print("\n",seq," is an Arithmetic Progression, with a common difference of ",diff)
        print("\n Next Number in sequence: ",seq[-1] + diff) 

    if GPCheck(seq):
        ratio = seq[-1] / seq[-2]   
        print("\n",seq," is an Geometric Progression, with a common ratio of ",ratio)
        print("\n Next Number in sequence: ",seq[-1] * ratio) 
        
def APCheck(seq: list):
    diff = seq[1] - seq[0]
    for i in range(2,len(seq)):
        temp = seq[i] - seq[i-1]
        if temp != diff:
            return False
    return True

def GPCheck(seq: list):
    diff = seq[1] / seq[0]
    for i in range(2,len(seq)):
        temp = seq[i] / seq[i-1]
        if temp != diff:
            return False
    return True

if __name__ == "__main__":
    idenProg([3, 5, 7, 9, 11, 13]) #Is an AP
    idenProg([2, 6, 18, 54]) #Is a GP
    idenProg([1,1,1,1,1]) 
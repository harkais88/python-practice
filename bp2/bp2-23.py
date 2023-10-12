#!/usr/bin/python3

"""Write a Python program to create a sequence where the first four members of the sequence 
are equal to one. Each successive term of the sequence is equal to the sum of the four previous ones. 
Find the Nth member of the sequence."""

def seqGen(n):
    if n == 0:
        return 0
    
    if n < 4:
        return 1
    
    seq = [1,1,1,1]

    for i in range(n-4):
        seq.append(seq[i] + seq[i+1] + seq[i+2] + seq[i+3])

    return seq[-1]

if __name__ == "__main__":
    # Expected Output: Sequence: 1 1 1 1 4 7, 6th Term: 7
    print(seqGen(6))
    

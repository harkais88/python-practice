#!/usr/bin/python3

"""Write a Python program to check whether a given sequence is linear, quadratic or cubic.
Sequences are sets of numbers that are connected in some way.
Linear sequence:
If a sequence has a common difference, it is called a linear sequence. 
Quadratic sequence:
If a sequence has a 2nd common difference, it is called a linear sequence. 
Cubic sequence:
If a sequence has a 3rd common difference, it is called a linear sequence. 
Sample Output:
Original Sequence: [0, 2, 4, 6, 8, 10]
Check the said sequence is Linear, Quadratic or Cubic?
Linear Sequence
Original Sequence: [1, 4, 9, 16, 25]
Check the said sequence is Linear, Quadratic or Cubic?
Quadratic Sequence
Original Sequence: [0, 12, 10, 0, -12, -20]
Check the said sequence is Linear, Quadratic or Cubic?
Cubic Sequence
Original Sequence: [1, 2, 3, 4, 5]
Check the said sequence is Linear, Quadratic or Cubic?
Linear Sequence"""

def checkSeq(nums):
    print("Original Sequence: ",nums)
    print("Check the said sequence is Linear, Quadratic or Cubic?")
    diff1 = [nums[i] - nums[i-1] for i in range(1,len(nums))]
    if len(set(diff1)) == 1:
        print("Linear Sequence")
    else:
        diff2 = [diff1[i] - diff1[i-1] for i in range(1,len(diff1))]
        if len(set(diff2)) == 1:
            print("Quadratic Sequence")
        else:
            diff3 = [diff2[i] - diff2[i-1] for i in range(1,len(diff2))]
            if len(set(diff3)) == 1:
                print("Cubic Sequence")
            else:
                print("Not a valid sequence")

if __name__ == "__main__":
    checkSeq([0, 2, 4, 6, 8, 10])
    checkSeq([1, 4, 9, 16, 25])
    checkSeq([0, 12, 10, 0, -12, -20])
    checkSeq([1, 2, 3, 4, 5])
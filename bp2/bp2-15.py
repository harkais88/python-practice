#!/usr/bin/python3

"""Write a Python program to check the priority of the four operators (+, -, *, /)."""

# * and / have the same priority
# + and - have the same priority
# * and / have a higher precedence than + and -
    
operator = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1
    }

def priority_check(op1, op2):
    print(f" Does {op1} have a higher precedence than {op2}? ",operator[op1] >= operator[op2])

if __name__ == "__main__":
    priority_check("+","*")
    priority_check("-","*")
    priority_check("/","+")
    priority_check("/","-")

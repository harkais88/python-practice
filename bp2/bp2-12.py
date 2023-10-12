#!/usr/bin/python3

"""Write a Python program that generates a list of all possible permutations 
from a given collection of distinct numbers."""

count = 0

def permutation(list):
    global count    
    print("Function Call ",count + 1, " for list ",list,": ")
    fc = count + 1 
    count += 1

    if len(list) == 0:
        print("Returning empty list")
        return []
    
    if len(list) == 1:
        print("Returning ",[list])
        return [list]
    
    perm_list = []

    for i in range(len(list)):
        print("Iteration ",i+1," for function call ", fc, ": ")
        m = list[i]
        print("m = ",m)

        remList = list[:i] + list[i+1:]
        print("remList = ",remList)

        for p in permutation(remList):
            print("Appending ",[m] + p," to perm_list")
            perm_list.append([m] + p)
            print("Current perm_list: ",perm_list)
    print("Returning ",perm_list," from function call ",fc)
    return perm_list

if __name__ == "__main__":
    list = [1,2,3]

    print(permutation(list))
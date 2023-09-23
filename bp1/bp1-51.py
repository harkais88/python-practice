"""Write a Python program to determine the profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long 
various parts of the program executed. These statistics can be formatted into reports via the pstats module."""

import cProfile

def sort(list):
    length = len(list)
    for i in range(length):
        for j in range(i+1,length):
            if list[j] < list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    return list

def main():
    list = [3,4,1,2]
    list = sort(list)
    print(list)

if __name__ == "__main__":
    cProfile.run('main()')    

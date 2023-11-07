#!/usr/bin/python3

"""Write a Python program to find the longest common prefix string 
among a given array of strings. Return false if there is no common prefix.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
Sample Input:
["abcdefgh","abcefgh"]
["w3r","w3resource"]
["Python","PHP", "Perl"]
["Python","PHP", "Java"]
Sample Output:
abc
w3r
P"""

def getLongestPrefix(list):
    if not list:
        return [""]
    
    min_length_word = min(list, key=len)

    for index,char in enumerate(min_length_word):
        for other in list:
            if other[index] != char:
                return min_length_word[:index]
            
    return min_length_word

if __name__ == "__main__":
    print(getLongestPrefix(["abcdefgh","abcefgh"]))
    print(getLongestPrefix(["w3r","w3resource"]))
    print(getLongestPrefix(["Python","PHP", "Perl"]))
    print(getLongestPrefix(["Python","PHP", "Java"]))
#!/usr/bin/python3

"""In mathematics, a subsequence is a sequence that can be derived 
from another sequence by deleting some or no elements without changing 
the order of the remaining elements. For example, the sequence (A,B,D)
is a subsequence of (A,B,C,D,E,F) obtained after removal of elements C, 
E, and F. The relation of one sequence being the subsequence of another 
is a preorder. The subsequence should not be confused with substring 
(A,B,C,D) which can be derived from the above string (A,B,C,D,E,F) by 
deleting substring (E,F). The substring is a refinement of the subsequence.
The list of all subsequences for the word "apple" would be "a", "ap", 
"al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", 
"p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
Write a Python program to find the longest word in a set of words which is a subsequence of a given string.
Sample Input:
("Green", {"Gn", "Gren", "ree", "en"})
("pythonexercises", {"py", "ex", "exercises"})
Sample Output:
Gren
exercises"""

# There are two ways in which we could get all subsequences of a given string
# The recursive way
# def subsequencer(string):
#     if len(string) == 0:
#         return [""]
    
#     first_char = string[0]
#     remaining_subsequences = subsequencer(string[1:])
#     current_subsequences = []

#     for subsequence in remaining_subsequences:
#         current_subsequences.append(subsequence)
#         current_subsequences.append(first_char + subsequence)

#     return set(current_subsequences)

# Or the iterative way
def subsequencer(string):
    subsequences = [""]

    for char in string:
        current_subsequences = []
        for subsequence in subsequences:
            current_subsequences.append(subsequence)
            current_subsequences.append(subsequence+char)
        subsequences = current_subsequences

    return set(subsequences)

def longestSubsequence(string, sset):
    # Just to make sure we don't just consider the same string as the longest one
    sset.remove(string)

    max_len = 0
    max_words = [""]

    for ele in sset:
        if len(ele) >= max_len:
            max_len = len(ele)
            if len(max_words[0]) < max_len:
                max_words = []
            max_words.append(ele)

    return max_words

if __name__ == "__main__":
    string1 = "Green"
    string2 = "pythonexercises"
    string3 = "India"

    print(longestSubsequence(string1,subsequencer(string1)))
    print(longestSubsequence(string2,subsequencer(string2)))
    print(longestSubsequence(string3,subsequencer(string3)))
#!/usr/bin/python3

"""In abstract algebra, a group isomorphism is a function between two groups that sets up 
a one-to-one correspondence between the elements of the groups in a way that respects the 
given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
Two strings are isomorphic if the characters in string A can be replaced to get string B
Given "foo", "bar", return false.
Given "paper", "title", return true.
Write a Python program to check if two given strings are isomorphic to each other or not.
Sample Input:
("foo", "bar")
("bar", "foo")
("paper", "title")
("title", "paper")
("apple", "orange")
("aa", "ab")
("ab", "aa")
Sample Output:
False
False
True
True
False
False
False"""

# A longer form of how to do it
# def isIsomorphic(A,B):
#     m = len(A)
#     n = len(B)

#     if m != n:
#         return False
    
#     mappings = {}

#     for i in range(m):
#         if A[i] not in mappings.keys():
#             if B[i] in mappings.values():
#                 return False
#             else:
#                 mappings[A[i]] = B[i]
#         else:
#             if mappings[A[i]] != B[i]:
#                 return False
            
#     return True

# The python way, does the exact same as given above
def isIsomorphic(A,B):
    return len(set(A)) == len(set(B)) == len(set(zip(A,B)))

if __name__ == "__main__":
    print(isIsomorphic("foo","bar"))
    print(isIsomorphic("bar","foo"))
    print(isIsomorphic("paper","title"))
    print(isIsomorphic("title","paper"))
    print(isIsomorphic("apple","orange"))
    print(isIsomorphic("aa","ab"))
    print(isIsomorphic("ab","aa"))
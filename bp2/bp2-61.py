#!/usr/bin/python3

"""Internet search engine giant, such as Google accepts web pages around the world 
and classify them, creating a huge database. The search engines also analyze the search 
keywords entered by the user and create inquiries for database search. In both cases, 
complicated processing is carried out in order to realize efficient retrieval, but basics 
are all cutting out words from sentences.
Write a Python program to cut out words of 3 to 6 characters length from a given sentence 
not more than 1024 characters.
Input:
English sentences consisting of delimiters and alphanumeric characters are given on one line.
Input a sentence (1024 characters. max.)
The quick brown fox
3 to 6 characters length of words:
The quick brown fox"""

if __name__ == "__main__":
    string = input("Input a sentence (1024 characters. max.)\n").replace(".","").replace(",","")
    print("3 to 6 characters length of words:\n"," ".join([word for word in string.split() if 3 <= len(word) <= 6]))
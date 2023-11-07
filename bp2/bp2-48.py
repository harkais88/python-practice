#!/usr/bin/python3

"""Write a Python program that reads text (only alphabetical characters and spaces) and prints two words. 
The first word is the one that appears most often in the text. The second one is the word with the most letters.
Note: A word is a sequence of letters which is separated by the spaces.

Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation."""

if __name__ == "__main__":
    text = input("Input text: ").split()

    words_count = {}
    max_len_word = text[0]

    for word in text:
        if word not in words_count.keys():
            words_count[word] = 1
        else:
            words_count[word] += 1
        
        if len(word) > len(max_len_word):
            max_len_word = word

    max = list(words_count.keys())[0]
    for word in list(words_count.keys())[1:]:
        if words_count[word] > words_count[max]:
            max = word

    print("Output: {} {}".format(max,max_len_word))
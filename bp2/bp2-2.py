#!/usr/bin/python3

"""Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'u'. 
Ensure that each character is used only once."""

from random import choice

if __name__ == "__main__":
    letters = ["a","e","i","o","u"]

    # Since each character should be used only once, we can assume 
    # that the question wants us to create all possible 5-letter strings 
    # using these letters. 

    # We know that there would be a total of 120 possible 5-letter words
    # with these five letters only without repetition

    # One horrible way to do it
    words = []
    count = 0 
    while count < 120:
        word = ""
        while True:
            letter = choice(letters)
            if letter not in word:
                word += letter
            if len(word) == 5:
                break
        if word not in words:
            words.append(word)
            count += 1

    print(" All possible 5 letter words with {}: {}".format(letters, ", ".join(words)))

    # This way makes sure to get all possible strings, but there are also a lot of redundant checks
    # I have recorded the while loop here to have looped 851 times, and while this is not the average,
    # it still loops around 500 times to get the unique strings  

    # The Python way
    from itertools import permutations

    print(" All possible 5 letter words with {}: {}".format(letters,
                                                        " ,".join(["".join(p) for p in permutations("aeiou",5)])))

    # Since we are using an inbuilt module, which happens to use C, it will be much faster than our python code
    # Check out the execution times using default_timer()
"""Write a Python program to get a newly-generated string from a given string where "Is" has 
been added to the front. Return the string unchanged if the given string already begins with "Is"."""

if __name__ == "__main__":
    string = input("\n Enter a string: ")

    if string[:2] != "Is":
        string = "Is" + string

    print(" Result: ",string)
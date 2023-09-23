"""Write a Python program to get the ASCII value of a character."""

if __name__ == "__main__":
    while True:
        char = input("\n Input a character: ")
        if len(char) == 1:
            break
        print("\n Input single character")

    print(" ASCII Value of {}: {}".format(char,ord(char)))
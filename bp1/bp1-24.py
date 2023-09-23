"""Write a Python program to test whether a passed letter is a vowel or not."""

if __name__ == "__main__":
    while True:
        char = input("\n Enter a letter: ")
        if len(char) > 1:
            print("\n Enter only one letter")
        else:
            break

    print("\n "+char+" is a vowel" if char.lower() in ["a","e","i","o","u"] else "\n "+char+" is not a vowel")
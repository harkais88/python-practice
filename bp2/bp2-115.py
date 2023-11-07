#!/usr/bin/python3

"""Write a Python program to print letters from the English alphabet from a-z and A-Z.
Sample Input:
("Alphabet from a-z:")
("\nAlphabet from A-Z:")
Sample Output:
Alphabet from a-z:
a b c d e f g h i j k l m n o p q r s t u v w x y z
Alphabet from A-Z:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"""

if __name__ == "__main__":
    print("Alphabet from a-z:")
    print(" ".join([chr(i) for i in range(97,123)]))
    print("Alphabet from A-Z:")
    print(" ".join([chr(i) for i in range(65,91)]))
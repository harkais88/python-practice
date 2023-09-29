#!/usr/bin/python3

"""Write a Python program to print Unicode characters."""

if __name__ == "__main__":
    #If you happen to know the unicode code points, you can print them like this
    print("\n Printing my name using code points: ",end="")
    print(u"\u0041\u0072\u006B\u0061 \U0001F60F") #u for 4 bit, U for 8 bit, I think

    str = "Arka"

    # Getting str in unicode (Credit: GeekforGeeks)
    print("\n Representing Unicode code point of each character of {}: {}\n".format(str, " ".join(r"\u{:04X}".format(ord(char)) for char in str)))
    # %04x is a format specifier, which only makes sense with the % operator. It specifies that the number to be formatted (in this case, ord(c)) 
    # should be formatted as a hexadecimal with four digits and zero-padding on the left. Ex: if c is "A", whose unicode point is 65, is printed as 0041

    # Another way to do this
    # import re
    # print(re.sub(".", lambda x: r"\u %X" % ord(x.group()), str))

    # Printing the unicode characters as string
    unicode_str = " ".join(r"\u{:04X}".format(ord(char)) for char in str)
    # To get back the string, we first encode the code points to their equivalent bytes (Converting to decimal I think), and then we decode the bytes as 
    # characters in accordance to the codec passed as parameter
    unicode_str = ''.join(char.encode().decode('unicode_escape') for char in unicode_str.split())

    print(" Printing the string again: ",unicode_str,end="\n\n")

    # To understand how these work, check out this article on unicode: 
    # https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
    # Gives an excellent basic understanding of unicode and the importance of it

    # Keep in mind that all Python strings as of Python 3 follows UTF-8 encoding
#!/usr/bin/python3

"""Write a Python program to print Emojis using Unicode characters or 
CLDR (Common Locale Data Repository) short names.

Hint: You may want to look up the unicode for them"""

# Emoji CLDR                     Unicode
# Smiling face with heart eyes   U+1F60D
# Unamused face                  U+1F612
# Beaming face with smiling eyes U+1F601
# Grinning face with sweat       U+1F605
# Face with tears of joy         U+1F602
# Slightly smiling face          U+1F642
# Smiling face with halo         U+1F607
# Zipper-mouth face              U+1F910
# Grinning Face                  U+1F600
# Rolling on the floor laughing  U+1F923

# Using The Unicodes
# if __name__ == "__main__":
#     print("Smiling face with heart eyes")
#     print("\U0001F60D")
#     print("Unamused face")
#     print("\U0001F612")
#     print("Beaming face with smiling eyes")
#     print("\U0001F601")
#     print("Grinning face with sweat")
#     print("\U0001F605")
#     print("Face with tears of joy")
#     print("\U0001F602")
#     print("Slightly smiling face")
#     print("\U0001F642")
#     print("Smiling face with halo")
#     print("\U0001F607")
#     print("Zipper-mouth face")
#     print("\U0001F910")
#     print("Grinning Face")
#     print("\U0001F600")
#     print("Rolling on the floor laughing")
#     print("\U0001F923")

# OR we could use the CLDR lookups
if __name__ == "__main__":
    print("Rolling on the floor laughing:")
    print("\N{rolling on the floor laughing}")
    print("Smiling face with halo:")
    print("\N{smiling face with halo}")
    print("Unamused face:")
    print("\N{unamused face}")
    print("Grinning face:")
    print("\N{grinning face}")
    print("Loudly crying face:")
    print("\N{loudly crying face}")
    print("Face with tears of joy:")
    print("\N{face with tears of joy}")
    print("Slightly smiling face:")
    print("\N{slightly smiling face}")
    print("Angry face:")
    print("\N{angry face}")
    print("Zipper-mouth face:")
    print("\N{zipper-mouth face}")
    print("Smiling face with sunglasses:")
    print("\N{smiling face with sunglasses}")
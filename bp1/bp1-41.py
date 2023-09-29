#!/usr/bin/python3

"""Write a Python program to check whether a file exists."""

# One Way to do it
# import os

# if __name__ == "__main__":
#     file_url = os.path.normpath(input("\n Enter the filename: "))
#     print("\n Finding the file ",file_url)
    
#     try:
#         file = open(file_url, "r")
#         print(" File Found Successfully")
#         file.close()
#     except FileNotFoundError:
#         print("\n File Not Found")

#Another way

import os

if __name__ == "__main__":
    file_url = os.path.normpath(input("\n Enter the filename: "))
    print("\n Finding the file ",file_url)

    print("\n File Exists? ",os.path.isfile(file_url))
    print("\n File Exists? ",os.path.exists(file_url))
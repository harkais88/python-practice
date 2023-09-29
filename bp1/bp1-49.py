#!/usr/bin/python3

"""Write a Python program to list all files in a directory."""

import os

if __name__ == "__main__":
    root = os.path.realpath(input("\n Enter the directory Name: "))

    for dirpath,dirnames,filenames in os.walk(root):
        #For viewing all directories inside specified directory
        # for dirname in dirnames:
        #     path = os.path.join(dirpath,dirname)
        #     print(path)
        for file in filenames:
            path = os.path.join(dirpath,file)
            print(path)

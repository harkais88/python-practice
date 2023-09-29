#!/usr/bin/python3

"""Write a Python program to check whether a file path is a file or a directory."""

import os

if __name__ == "__main__":
    file_paths = []

    for dirpath,dirnames,filenames in os.walk("C:\\Users\\arka_\\Documents\\Python Scripts"):
        for dir in dirnames:
            path = os.path.join(dirpath,dir)
            file_paths.append(path)

        for file in filenames:
            path = os.path.join(dirpath,file)
            file_paths.append(path)

    for file_path in file_paths:
        print(file_path,end=" ")
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                print("is a directory")
            if os.path.isfile(file_path):
                print("is a file")
        else:
            print("does not exist")
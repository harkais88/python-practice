#!/usr/bin/python3

"""Write a Python program to find the path to a file or directory when you encounter a path name. """

import os

if __name__ == "__main__":
    # Replace path var with any path that contains files or directories
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for file in os.listdir(path):
        file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file)
        print("NAME: ",file)
        print("Does it exist? ",os.path.exists(file))
        if os.path.exists(file):
            print("Is it a file? ",os.path.isfile(file))
            print("Is it a directory? ",os.path.isdir(file))
            print("Is it an absolute path? ",os.path.isabs(file))
            print("Is it a link? ", os.path.islink(file))
            print("Does the link exist? ",os.path.lexists(file))


#!/usr/bin/python3

"""Write a Python program to retrieve file properties. """

import os

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    
    print("File Name: ", os.path.basename(script_path))
    print("Created: ",os.path.getctime(script_path))
    print("Accessed: ",os.path.getatime(script_path))
    print("Modified: ",os.path.getmtime(script_path))
    print("Size: ",os.path.getsize(script_path))
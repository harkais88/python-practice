#!/usr/bin/python3

"""Write a Python program to clear the screen or terminal."""

import os
from time import sleep

if __name__ == "__main__":
    print("Going to clear screen in 3 seconds: ")
    sleep(3)
    os.system('cls')
#!/usr/bin/python3

"""Write a Python program to get system command output."""

import subprocess

if __name__ == "__main__":
    returned_text = subprocess.check_output("dir",shell=True,universal_newlines=True)
    print(returned_text)    
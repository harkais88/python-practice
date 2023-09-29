#!/usr/bin/python3

"""Write a Python program to get OS name, platform and release information."""

import platform,os

if __name__ == "__main__":
    print("\n OS Name: ",os.name)
    print("\n OS Platform: ",platform.platform())
    print("\n OS system: ",platform.system())
    print("\n Os Release Info: ",platform.release())
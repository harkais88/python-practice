#!/usr/bin/python3

"""Write a Python program to get the effective group id, effective user id, real group id, 
and a list of supplemental group ids associated with the current process.
Note: Availability: Unix."""

import os

if __name__ == "__main__":
    print("\n Effective group ID: ",os.getegid())
    print("\n Effective user ID: ",os.geteuid())
    print("\n Real Group ID: ",os.getgid())
    print("\n List of supplemental group ids associated with the current process: ",os.getgroups())
#!/usr/bin/python3

"""Write a Python program to get the users environment. """

import os

if __name__ == "__main__":
    print("\nUser {}'s environment: {}\n".format(os.environ["USER"],os.environ))

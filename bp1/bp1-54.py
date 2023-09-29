#!/usr/bin/python3

"""Write a Python program to get the current username."""

import os

if __name__ == "__main__":
    print(os.environ["USERNAME"])

#OR

# import getpass

# if __name__ == "__main__":
#     print(getpass.getuser())

#OR

#This will only work on Unix Systems
# import os 
# import pwd

# if __name__ == "__main__":
#     print(pwd.getpwuid( os.getuid() )[ 0 ])
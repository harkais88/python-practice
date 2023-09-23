"""Write a Python program to get the command-line arguments (name of the script, 
the number of arguments, arguments) passed to a script."""

import sys

if __name__ == "__main__":
    print("\n The system arguments, along with the path: ",sys.argv)
    print("\n Just the path name: ",sys.argv[0])
    print("\n Just the arguments passed given at command line: ",sys.argv[1:])
#!/usr/bin/python3

"""Write a NumPy program to get help with the add function."""

import numpy as np

if __name__ == "__main__":
    # One way to do it
    #print(help(np.add))
    
    # OR

    # Another way to do it
    print(np.info(np.add))  
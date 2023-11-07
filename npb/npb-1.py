#!/usr/bin/python3

"""Write a Numpy program to get the Numpy version and show the Numpy build configuration."""

import numpy as np

if __name__ == "__main__":
    print("Numpy version: ",np.__version__)
    print("Numpy build configuration:\n",np.show_config())
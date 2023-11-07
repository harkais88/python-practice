#!/usr/bin/python3

"""Write a NumPy program to generate a uniform, 
non-uniform random sample from a given 1-D array with and without replacement."""

import numpy as np

if __name__ == "__main__":
    np.random.seed(10)
    print("Generate a uniform random sample with replacement:") 
    print(np.random.choice(7, 5))
    print("\nGenerate a uniform random sample without replacement:") 
    print(np.random.choice(7, 5, replace=False))
    print("\nGenerate a non-uniform random sample with replacement:")  
    print(np.random.choice(7, 5, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1])) #p here is probability
    print("\nGenerate a uniform random sample without replacement:") 
    print(np.random.choice(7, 5, replace=False, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1])) 
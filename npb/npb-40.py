#!/usr/bin/python3

"""Write a NumPy program to compute the x and y coordinates for 
points on a sine curve and plot the points using matplotlib."""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.arange(0,3*np.pi,0.2)
    y = np.sin(x)

    plt.plot(x,y)
    plt.title("Sine Curve")
    plt.show()
#!/usr/bin/python3

"""Write a program to compute the radius and the central coordinate (x, y) of a circle 
which is constructed from three given points on the plane surface.
Input:
x1, y1, x2, y2, x3, y3 separated by a single space.
Input three coordinate of the circle:
9 3 6 8 3 6
Radius of the said circle:
3.358
Central coordinate (x, y) of the circle:
6.071 4.643"""

# So, we know that the general equation of a circle can be given as:
# x^2 + y^2 + 2ax + 2by + c = 0
#
# Since the points (x1,y1), (x2,y2) and (x3,y3) have to lie on the same circle,
# we can consider the following set of equations as a system together:-
#
# x1^2 + y1^2 + 2ax1 + 2by1 + c = 0
# x2^2 + y2^2 + 2ax2 + 2by2 + c = 0
# x3^2 + y3^2 + 2ax3 + 2by3 + c = 0
#
# It goes to show that if this system does not have any solution, the points 
# cannot be on the same circle
#
# Knowing x1,y1,x2,y2,x3,y3, we can rewrite the above system can then be written as the following:-
#
# 2ax1 + 2by1 + c = - (x1^2 + y1^2)
# 2ax2 + 2by2 + c = - (x2^2 + y2^2)
# 2ax3 + 2by3 + c = - (x3^2 + y3^2)
#
# which can be rewritten as:-
#
# | 2x1 2y1 1 | | a | = | - (x1^2 + y1^2) |
# | 2x2 2y2 1 | | b |   | - (x2^2 + y2^2) |
# | 2x3 2y3 1 | | c |   | - (x3^2 + y3^2) |
#
# Therefore,
#
# | a | = ( | 2x1 2y1 1| )^ -1 . | - (x1^2 + y1^2) |
# | b |     | 2x2 2y2 1|         | - (x2^2 + y2^2) |
# | c |     | 2x3 2y3 1|         | - (x3^2 + y3^2) | 
#
# => | a | = __1__ . |   (2y2 - 2y3)     (2y3 - 2y1)     (2y1 - 2y2)   | . | - (x1^2 + y1^2) |   
#    | b |    det    |   (2x3 - 2x2)     (2x1 - 2x3)     (2x2 - 2x1)   |   | - (x2^2 + y2^2) |
#    | c |           | (4x2y3 - 4x3y2) (4x3y1 - 4x1y3) (4x1y2 - 4x2y1) |   | - (x3^2 + y3^2) | 
#
# where det = 4x1y2 - 4x1y3 - 4x2y1 + 4x3y1 + 4x2y3 - 4x3y2
#
# We also know that coordinates of center of circle and its radius can then be given as the following:-
# 
# Xc = -a
# Yc = -b
# R = sqrt( Xc^2 + Yc^2 - c) 

from math import pow,sqrt

if __name__ == "__main__":
    print("\nInput three coordinate of the circle:")
    x1,y1,x2,y2,x3,y3 = [float(i) for i in input().split()]

    det = 4 * ( (x1*y2) - (x1*y3) - (x2*y1) + (x3*y1) + (x2*y3) - (x3*y2) )

    if det == 0:
        print("\nGiven Coordinates cannot lie on the same circle")
        print()
    else:
        a = (1/det) * ( (((2*y2) - (2*y3)) * (-(pow(x1,2) + pow(y1,2)))) + 
                        (((2*y3) - (2*y1)) * (-(pow(x2,2) + pow(y2,2)))) +
                        (((2*y1) - (2*y2)) * (-(pow(x3,2) + pow(y3,2)))) )
        
        b =  (1/det) * ( (((2*x3) - (2*x2)) * (-(pow(x1,2) + pow(y1,2)))) + 
                        (((2*x1) - (2*x3)) * (-(pow(x2,2) + pow(y2,2)))) +
                        (((2*x2) - (2*x1)) * (-(pow(x3,2) + pow(y3,2)))) )
        
        c =  (1/det) * ( (((4*x2*y3) - (4*x3*y2)) * (-(pow(x1,2) + pow(y1,2)))) + 
                        (((4*x3*y1) - (4*x1*y3)) * (-(pow(x2,2) + pow(y2,2)))) +
                        (((4*x1*y2) - (4*x2*y1)) * (-(pow(x3,2) + pow(y3,2)))) )
        
        xc = -a
        yc = -b
        R = sqrt( xc ** 2 + yc ** 2 - c)

        print("Radius of said circle:")
        print(round(R,ndigits=3))
        print("Central coordinate (x, y) of the circle:")
        print(f"{round(xc,ndigits=3)} {round(yc,ndigits=3)}\n")
#!/usr/bin/python3

"""Write a Python program which solve the equation:
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
Input:
a,b,c,d,e,f separated by a single space.
(-1,000 <= a,b,c,d,e,f <= 1,000)
Input the value of a, b, c, d, e, f:
5 8 6 7 9 4
Values of x and y:
-2.000 2.000"""

# There are multiple ways of doing this
# For this one, let's try matrix form

# ax + by = c, dx + ey = f
# Can be also rewritten as |a b|.|x| = |c|
#                          |d e| |y| = |f|
# 
# Therefore, |x| = |a b|^-1 . |c|
#            |y|   |d e|      |f|
#
#         => |x| = ____1____ . |e -b| . |c|
#            |y| = (ae - bd)   |-d a|   |f|
#
#         => |x| = ____1____ . |ec - bf|
#            |y| = (ae - bd)   |-dc + af|
#
# Therefore, x = ____1____ x (ec - bf)
#                (ae - bd)
#
#            y = ____1____ x (-dc + af)
#                (ae - bd)
#
# Thus, we can simply our code using a few linear relationships!
# Note: This will not work if ae - bd = 0. For this case, we will first check that
# If ae - bd = 0, the equations have either infinite or no solutions.

def pairSolve(a,b,c,d,e,f):
    print(f"\n Given Equations: \n {a}x + {b}y = {c} \n {d}x + {e}y = {f}")

    det = a*e - b*d # This happens to be the determinant of the matrix
    print(f" Determinant of [({a} {b}),({d} {e})] = {det}")

    if det == 0:
        print(" Equations either have infinite solutions, or has no solution")
        # We could find this out, but for this program, let's ignore that
    else:
        x = (1/det) * ((e*c) - (b*f))
        y = (1/det) * ((a*f) - (d*c))

        print(f" x = {x}, y = {y}")

if __name__ == "__main__":
    print(" Equations format \n ax + by = c \n dx + cy = f")
    print(" Input the value of a,b,c,d,e,f: ")
    a,b,c,d,e,f = [int(i) for i in input().split()]
    pairSolve(a,b,c,d,e,f)
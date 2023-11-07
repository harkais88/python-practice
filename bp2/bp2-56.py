#!/usr/bin/python3

"""There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys). 
Write a Python program to determine whether AB and CD are orthogonal.
Input:
xp,yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value 
can be up to 5 digits after the decimal point It is given as a real number including the number of. Output:
Output AB and CD are not orthogonal! or AB and CD are orthogonal!."""

# We determine if two lines are orthogonal by looking at their slopes
# If both have infinite slopes, then no
# If one has infinite slope, and the other has 0, then yes
# If both have finite slope, and their product is -1, then yes

def isOrthogonal(xp,yp,xq,yq,xr,yr,xs,ys):
    # If both have infinite slope
    if (xq - xp == 0) and (xs - xr == 0):
        return False
    
    # If one has infinite slope and the other has 0
    if (xq - xp == 0):
        m = (ys - yr) / (xs - xr)
        if m == 0:
            return True
        else:
            return False
        
    if (xs - xr == 0):
        m = (yq - yp) / (xq - xp)
        if m == 0:
            return True
        else:
            return False
        
    m1 = (yq - yp) / (xq - xp)
    m2 = (ys - yr) / (xs - xr)
    if (m1 * m2 == -1):
        return True
    return False

if __name__ == "__main__":
    print("Input xp,yp,xq,yq,xr,yr,xs,ys [P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys)] comma seperated:")
    xp,yp,xq,yq,xr,yr,xs,ys = [float(i) for i in input().split(",")]

    print("AB and CD are not orthogonal" if not isOrthogonal(xp,yp,xq,yq,xr,yr,xs,ys)
          else "AB and CD are orthogonal")

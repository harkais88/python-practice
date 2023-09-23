"""Write a Python program to calculate the midpoints of a line."""

if __name__ == "__main__":
    x1,y1 = [float(i) for i in input("\n Enter the coordinates x1,y1: ").split(",")]
    x2,y2 = [float(i) for i in input("\n Enter the coordinates x2,y2: ").split(",")]

    print("\n Midpoint of the line from {},{} to {},{}: {},{}".format(x1,y1,
                                                                      x2,y2,
                                                                      (x1+x2)/2,
                                                                      (y1+y2)/2))

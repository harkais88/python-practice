"""Write a Python program to sort three integers without explicitly using conditional statements and loops."""

if __name__ == "__main__":
    x,y,z = [int(i) for i in input("\n Enter the three integers seperated by commas: ").split(",")]

    a3 = max(x,y,z)
    a1 = min(x,y,z)
    a2 = (x+y+z) - a1 - a3
    
    print("\n The sorted integers: {} {} {}".format(a1,a2,a3))
"""Write a Python program to add two objects if both objects are integers."""

def chck(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    return -1

if __name__ == "__main__":
    n1,n2 = 1,2
    n3,n4 = 1,2.0

    print(chck(n1,n2))    
    print(chck(n3,n4))
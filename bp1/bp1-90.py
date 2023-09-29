#!/usr/bin/python3

"""Write a Python program to create a copy of its own source code."""

import os
import time
#import pyuac

def main():
    src_path = os.path.abspath(__file__)
    dest_path = os.path.join(os.getcwd(),"test.txt")

    src = open(src_path,"r")
    dest = open(dest_path,"w")
    for line in src:
        dest.write(line)

    src.close()
    dest.close()

    with open(dest_path,"r") as dest:
        for line in dest:
            print(line,end="")

    print("\n Size of {}: {} bytes".format(src_path,os.path.getsize(src_path)))
    print("\n Check out the file test.txt in the current directory before it gets deleted")
    time.sleep(20)
    os.remove(dest_path)
    print("test.txt has been removed")    

if __name__ == "__main__":
    # if not pyuac.isUserAdmin():
    #     print("\n Relaunching as Admin!")
    #     pyuac.runAsAdmin()
    # else:
        main()
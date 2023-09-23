"""Write a Python program that retrieves the date and time of file creation and modification."""

import os,time

if __name__ == "__main__":
    file_name = "bp1-1.py"
    file_path = "./"+file_name

    print("\n Time of creation: ",time.ctime(os.path.getctime(file_path)))
    print("\n Time of modification: ",time.ctime(os.path.getmtime(file_path)))
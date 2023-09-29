#!/usr/bin/python3

"""Write a Python program to find out what version of Python you are using."""

#Using the sys module
# import sys

# if __name__ == "__main__":
#     print("Python Version")
#     print(sys.version)
#     print("Version Info")
#     print(sys.version_info)

#Using the platform module
import platform

if __name__ == "__main__":
    print("Python Version")
    print(platform.python_version())
    print("Version Info")
    v_info = platform.python_version_tuple()
    print("major = {}, minor = {}, patchlevel = {}".format(v_info[0],v_info[1],v_info[2]))
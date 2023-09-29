#!/usr/bin/python3

"""Write a Python program to print to STDERR."""
#Kind of a weird one to be honest, needs to be better explained

#The __future__ module is for accessing the new stuff that cannot be found in the previous versions
#It was mainly made for the Python 2.x version users to incorporate functionalities introduced in 
#Python 3.x

from __future__ import print_function 
import sys

#Note: * in a python function call denotes multiple non-keyword arguments passed to it without specifying 
#exactly how many. ** on the other hand is similar to *, only it is done for keyword arguments passed to it, like
#sep = "--". For remembering this, we use the variable names *args and **kwargs, kw being short for keyword.

def eprint(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs) #This is one of the ways of printing to the STDERR stream, by 
                                              #literally writing to the stderr file 

eprint("abc","def","ghi",sep = "--")
 
#!/usr/bin/python3

""" Write a Python program to validate an IP address. """

import socket

if __name__ == "__main__":
    ip1 = "127.0.0.1"
    ip2 = "127.0.0.300"

    try:
        socket.inet_aton(ip1)
        print(ip1, "is a valid IP Address")
    except OSError:
        print(ip1, "is not a valid IP Address")

    try:
        socket.inet_aton(ip2)
        print(ip2, "is a valid IP Address")        
    except OSError:
        print(ip2, "is not a valid IP Address")
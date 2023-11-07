#!/usr/bin/python3

"""Write a Python program to get the domain name using PTR DNS records from a given IP address.
Domain name using PTR DNS:
dns.google
ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com
dns.google
ec2-23-23-212-126.compute-1.amazonaws.com"""

import socket

def getDomain(addr):
    return socket.gethostbyaddr(addr)[0]

if __name__ == "__main__":
    print(getDomain("8.8.8.8"))
    print(getDomain("13.251.106.90"))
    print(getDomain("8.8.4.4"))
    print(getDomain("23.23.212.126"))

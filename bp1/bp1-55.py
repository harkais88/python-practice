#!/usr/bin/python3

"""Write a Python program to find local IP addresses using Python's stdlib."""

#... If you have no idea on how this worked, me neither :P. Better learn about sockets man

import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                    [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in 
                      [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
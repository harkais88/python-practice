"""Write a Python program to get the name of the host on which the routine is running."""

import socket

if __name__ == "__main__":
    print(socket.gethostname())

#.... Really need to study about socket programming, might come in handy later in life
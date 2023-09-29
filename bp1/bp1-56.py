#!/usr/bin/python3

"""Write a Python program to get the height and width of the console window."""

# #Another code that works only in Linux... maybe I should switch OS again

# import fcntl, termios, struct

# if __name__ == "__main__":
#     th, tw, hp, wp = struct.unpack("HHHH",
#                                fcntl.ioctl(0, termios.TIOCGWINSZ,
#                                            struct.pack("HHHH",0,0,0,0)))
#     print(tw,th)

#Or we could use the os get terminal size method... pretty useful stuff

import os

if __name__ == "__main__":
    print("\n Terminal Size: {}*{}".format(os.get_terminal_size()[0],os.get_terminal_size()[1]))
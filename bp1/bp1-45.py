"""Write a Python program that calls an external command."""

# import subprocess

# if __name__ == "__main__":
#     subprocess.call(["ls", "-l"])

from subprocess import call
call(["echo", "Hello", "World"],shell=True)
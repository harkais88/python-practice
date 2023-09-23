"""Write a Python program to locate Python site packages."""

#Shows where all the inbuilt Python binary modules are stored

import site

if __name__ == "__main__":
    for url in site.getsitepackages():
        print(url)
#!/usr/bin/python3

"""Write a Python program to access and print a URL's content to the console."""

#One way to do it

# from http.client import HTTPConnection

# if __name__ == "__main__":
#     website = "info.cern.ch"
#     path = "/hypertext/WWW/TheProject.html"
#     port = 80
#     connection = HTTPConnection(website,port)
#     connection.request("GET",path)
#     site = connection.getresponse()
#     content = site.read()
#     print(content)

#Or

import requests

if __name__ == "__main__":
    website = "info.cern.ch"
    path = "/hypertext/WWW/TheProject.html"
    data = requests.get("http://"+website+path)
    print(data.text)

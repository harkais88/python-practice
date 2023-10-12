#!/usr/bin/python3

"""Write a Python program that retrieves the top stories from Google News."""

# Requires requests, html5lib, and bs4 modules

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    news_url = "https://news.google.com"
    r = requests.get(news_url)

    soup = BeautifulSoup(r.content, "lxml")

    # Use this to check out the HTML content extracted
    # This is an important step as you need to check out
    # in which tags the Top Stories are given
    # print(soup.prettify())

    # Heck, maybe after a while, the rest of the code 
    # may not even work, so it is crucial you do the above print
    # It would be better to write the output to a file though, so 
    # if writing to a file, use the syntax file = open(file_path, "w", encoding = "utf-8")
    # to avoid encoding errors

    # NOTE: Not all content could be displayed using bs4, as it reads from static content
    # Sites like Google News dynamically load their content using Javascript
    # So, we would need a headless brower automation like Selenium for this

    # At the time of this script, I found that the stories seemed to be 
    # kept in h4 tags of the class gPFEn
    data = soup.find_all("h4", class_ = "gPFEn")

    print("**************************TOP STORIES TODAY****************************\n")
    for index, top_stories in enumerate(data, start = 1):
        print("*****************************************************************")
        print(f"{index}. {top_stories.text}\n")

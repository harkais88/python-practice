#!/usr/bin/python3

"""Write a Python program to make a request to a web page, and test the status code, 
and display the HTML code of the specified web page.
Sample Output:
Web page status: <Response [200]>
HTML code of the above web page:
<!doctype html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8" />
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>"""

import requests

if __name__ == "__main__":
    web_url = "https://www.iana.org/domains/example"
    r = requests.get(web_url)
    print("Web Page Status: ",r.status_code)
    print("HTML code of the above web page:")

    if r.ok:
        print(r.text)

    # OR Using BeautifulSoup
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(r.content)
    # print(soup.prettify())
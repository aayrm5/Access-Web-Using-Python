import ssl
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

num = []

for row in tags:
    n = row.contents[0]
    num.append(n)

n_int = []

for i in num:
    i = int(i)
    n_int.append(i)

print(sum(n_int))
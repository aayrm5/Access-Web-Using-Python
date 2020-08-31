import requests
from bs4 import BeautifulSoup

url = input("Enter Url: ")
xml_req = requests.get(url)
soup = BeautifulSoup(xml_req.text,'xml')

counts = soup.find_all('count')

c = []
for i in counts:
    c.append(int(i.text))

print(c)
print(sum(c))
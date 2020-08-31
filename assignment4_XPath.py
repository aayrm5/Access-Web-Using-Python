import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


ctx = ssl.create_default_context()
ssl.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the link:')
xml_doc = urllib.request.urlopen(url,context=ctx).read()

tree = ET.fromstring(xml_doc)

counts = tree.findall('.//count')

c = []
for i in counts:
    c.append(int(i.text))

print(c)
print(sum(c))
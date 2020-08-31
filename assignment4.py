# Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_921057.xml (Sum ends with 5)
# You are to look through all the tags and find the values sum the numbers.

import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the link:')
xml_doc = urllib.request.urlopen(url,context=ctx).read()

tree = ET.fromstring(xml_doc)

lst_count = tree.findall('comments/comment')

counts_num = []
for item in lst_count:
    counts_num.append(int(item.find('count').text))  

print(counts_num)

print(sum(counts_num))
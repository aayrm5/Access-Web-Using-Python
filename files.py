file_s = open('assign_sample.txt')
file_s.readline()

total_text = file_s.read() 
import re
a = re.findall('[0-9]+',total_text)
print(a)
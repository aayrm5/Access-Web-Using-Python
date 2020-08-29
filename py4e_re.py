
import re

hand = open('sample_text.txt')
for line in hand:
    line = line.rstrip()
    if re.findall('^From.*:',line):
        print(line)

x = 'My 2 fav numbers are 15 and 999'
y = re.findall('[0-9]+',x)
print(y)
z = re.findall('[AEIOU]+', x)
print(z)

a = re.findall('[aeiou]+', x)
print(a)

strng = 'From: Using the : character'
r = re.findall('^F.+:', strng)
# This is a greedy matching pattern as we specified + -> which is one or more times
# . -> any character; end with : is mentioned above.
print(r)  

r1 = re.findall('^F.+?:', strng)
# This is a non greedy matching pattern as ? is added above.
print(r1)

s = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

yy = re.findall('\S+@\S+', s)
# \S+ represents atleast one non-whitespace character
print(yy)

yy = re.findall('\S+?@\S+', s)
print(yy)

y1 = re.findall('^From\s(\S+@\S+)', s)
# \s - matches a whitespace char. () - extract the only the ex mentioned in it. 
print(y1)

hand = open('sample_text.txt',mode='r')
for line in hand:
    line = line.rstrip()
    if re.findall('^From:.*', line):
        print(line)

# pwd()

yee = re.findall('@([^ ]*)', s)
# @ -> start at @ in the line
# [^ ] -> match a non blank character (^shows negation that it should not match a blank)
# * -> match many of them.
print(yee) #['uct.ac.za']

# s = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

ze = re.findall('@(\S+)', s)
print(ze) #['uct.ac.za']

ze = re.findall('@\S.+', s)
print(ze) #['@uct.ac.za Sat Jan 5 09:14:16 2008']

ze = re.findall('@\S.+?', s)
print(ze) #['@uc']

ze = re.findall('@\S.', s)
print(ze) #['@uc']

ze = re.findall('@(\S*)', s)
print(ze) #['uct.ac.za']

ze = re.findall('.*', s)
print(ze) #['From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008', '']

ze = re.findall('.*?', s) #Non greedy method - Matches zero or more chars.
print(ze)

ze = re.findall('.+', s) # greedy method - Matches ONE or more chars.
print(ze) #returns entire string

ze = re.findall('\S+', s) # greedy method - Matches ONE or more word.
print(ze) #returns a list of each word - split at space.

ze = re.findall('\S+?', s) # non-greedy method - Matches ONE or more chars.
print(ze) #same as above.

####Another example
s1 = 'We just received $10.00 for cookies'
zz = re.findall('\$[0-9.]+', s1)
print(zz)


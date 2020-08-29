# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_921053.txt (There are 74 values and the sum ends with 173)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re

hand_act = open('assign_act.txt', 'r')

num =[]
for line in hand_act:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    for i in x:
        i = int(i)
        num.append(i)
print(sum(num))


# the above hussle in list comprehension
print(sum([int(i) for i in re.findall('([0-9]+)',open('assign_act.txt').read())]))
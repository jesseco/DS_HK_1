#!/usr/bin/python
# Import required libraries
from __future__ import division
import sys

"""
Right now the python script finds a sum of the impressions column. Update it to also return:
The average age in the file
Click through rate (avg clicks per impression)
The oldest person in the file
This should all be write out to the standard out using a few lines with "print"
When you have a python script that works, save it in your personal homework directory under lesson01 .
"""

# Start a counter and store the textfile in memory
age = 0
count = 0

lines = sys.stdin.readlines()
lines.pop(0)
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
  count = count + int(line.strip().split(',')[2])
  age = age + int(line.strip().split(',')[0])

print 'Total Unique Visitors:', n
print 'Total Impressions:', count
print 'Average Age:', age/n
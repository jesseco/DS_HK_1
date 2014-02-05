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
count = 0
impressions = 0
clicks = 0
lines = sys.stdin.readlines()
lines.pop(0)
oldest_person = [0]
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
  c_line = line.strip().split(',')
  age = int(c_line[0])
  count = count + int(c_line[2])
  if age > int(oldest_person[0]):
	oldest_person = c_line
	print oldest_person
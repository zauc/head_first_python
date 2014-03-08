#!/usr/bin/python

import os


#考虑分割符的个数，以及如果没有分割符  help(srt.split)
data = open('sketch.txt')
#print(data.readline(), end='')

for each_line in data:
    (role, line_spoken) = each_line.split(":", 1)
    print(role, end='')
    print(' said', end='')
    print(line_spoken, end='')

data.close()

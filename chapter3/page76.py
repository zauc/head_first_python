#!/usr/bin/python

import os

data = open('sketch.txt')
print(data.readline(), end='')

for each_line in data:
    print(each_line, end='')

data.close()

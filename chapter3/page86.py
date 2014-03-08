#!/usr/bin/python

import os


#用if去判断是否有:，然后进行处理，但是如果文件格式发生了变化，那代码还要进行修改
data = open('sketch.txt')
#print(data.readline(), end='')

for each_line in data:
    if not each_line.find(":") == -1:
        (role, line_spoken) = each_line.split(":", 1)
        print(role, end='')
        print(' said', end='')
        print(line_spoken, end='')

data.close()

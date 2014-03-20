#!/usr/bin/python3


with open('julie.txt', 'r') as juf:
	data = juf.readline()
julie = data.strip().split(',')
with open('james.txt', 'r') as jaf:
	data = jaf.readline()
james = data.strip().split(',')
with open('mikey.txt', 'r') as mif:
	data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt', 'r') as saf:
	data = saf.readline()
sarah = data.strip().split(',')


print(julie)
print(james)
print(mikey)
print(sarah)

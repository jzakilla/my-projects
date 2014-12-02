#!/usr/bin/python
import sys

searchstring = sys.argv[1]

filename = sys.argv[2]
myfile = open(filename)
lines = myfile.readlines()
myfile.close()

for line in lines:
	foundat = line.find(searchstring)
	if(foundat >= 0):
		print line.rstrip("\n")

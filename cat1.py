#!/usr/bin/python
import sys
filename = sys.argv[1]
myfile = open(filename)
lines = myfile.readlines()
myfile.close()
for line in lines:
	print line.rstrip("\n")


#!/usr/bin/python
import sys

def catfile(filename):
	myfile = open(filename)
	lines = myfile.readlines()
	myfile.close()
	for line in lines:
        	print line.rstrip("\n")

for filename in sys.argv[1:]:
	catfile(filename)



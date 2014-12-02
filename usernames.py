#!/usr/bin/python
import sys
#Print a list of usernames
filename = "/etc/shadow"
myfile = open(filename)
lines = myfile.readlines()
myfile.close()

PASSONLY = False
if(len(sys.argv)>1 and sys.argv[1]=='-p'):
	PASSONLY = True

for line in lines:
	#put code here
	tokens = line.split(':')
	if(PASSONLY):
		if(len(tokens[1])>1):
			print tokens[0:2]
	else:
		print tokens[0]

#!/usr/bin/python

import sys

PASSWORD = "swordfish"
print sys.argv[1:]

if(sys.argv[1]==PASSWORD):
	print "Access granted"
else:
	print "Access denied"
	sys.exit()

#!/usr/bin/python
import os
mylist = [1,2,3,4,5]
for i in mylist:
	print i * i
	print str(i) + " times " + str(i)

#for i in range(1,255):
#        os.system("ping -c 1 192.168.1.%d" % (i))

total = 0
for i in range(1, 15):
	total = total + i
	print "192.168.10.%03d" % (i)

userinput = raw_input("Please enter an integer number: ")
print "The number", userinput, "is equal to %x in hexadecimal." % int(userinput)



#!/usr/bin/env python

# reading and writing files

from sys import stdout

# reading from a text file line by line
with open('in1.txt') as f:
    n = 1
    for line in f:
        stdout.write('%d: %s' % (n, line))
        n += 1

# writing to a file
with open('out.txt','w') as f:
#with open('out.txt','a') as f:	# To append.
     f.write('hi there\n')
     f.write('here is some output\n')
     f.write(str(23))
     f.write('\n')

# reading comma separated values
import csv

with open('in2.csv') as f:
    for line in csv.reader(f):
        print(line)
	if int(line[0]) > 3: print(line)	# Python reads strings from files automatically...?

# changing delimiter
with open('in3.txt') as f:
    for line in csv.reader(f, delimiter=' '):
        pass # pass means to skip and do nothing.
	print(line)
# 
# read comma separated values with headings into a dictionary
with open('in4.csv') as f:
#    for line in csv.DictReader(f):
#           print(line)
#           print('Batch id: ' + line['batchID'])    
    everything = list(csv.DictReader(f))

print(everything[2]['sampleName'])
print(everything[2]['id'])
print('everything:',everything)



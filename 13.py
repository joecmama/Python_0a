#!/usr/bin/env python

# command-line arguments

# check python version
from sys import version_info
assert version_info[0] > 2 or (version_info[0] == 2 and version_info[1] > 6), 'python version must be 2.7 or later'
# 
from argparse import ArgumentParser
#  
desc = '''Here is a description of my program.
This might be long so I am putting this in a multiline string.
Three quote marks are used for that....'''
# 
# # default value for number of iterations
DEFAULT_N = 20 # convention - put constants in CAPS
# 
p = ArgumentParser(description=desc)
# 
# # an optional integer command line argument
p.add_argument('-n', type=int, help='number of iterations (default: %d)' % DEFAULT_N, default=DEFAULT_N)  # the "-" in "-n" means it's optional.
# 
# # a required string argument (one or more)
p.add_argument('file', nargs='+', help='input files') #nargs='+' means 1 or more.
# 
args = p.parse_args() # namespace of command line arguments
# 
print('number of iterations: %d' % args.n)
for f in args.file:
  print('I am going to process input file: %s' % f)
print(args)

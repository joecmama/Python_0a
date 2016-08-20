#!/usr/bin/env python

# # variables
a = 3.45
a = 12345678901234567890.12345678901234567890
b = a
b = 'hi there'
# 
# # formatted number: the 15 is the width, the 8 is the precision
#c = 'a = %15.8f' % a
c = 'a = %30.8f' % a
print(a)
print(c)
# 
# # string in a given width
print('b is the string |%20s|' % b) # right-justified
print('b is the string |%-20s|' % b) # left-justified
# 
# # multiple formats
print('a = %15.8f, b is "%s"' % (a,b))
# 
# # (decimal) integer
print('an integer: %5d' % 34)  # pad with spaces
print('an integer: %05d' % 34) # pad with zeros
# 
print('%12s %12s %12s' % ('a','little','table'))
print('%12f %12f %12f' % (23.23,3.234,234.23))
print('%12f %12f %12f' % (46.1,1.2322,34.34))

# Octal digits:
print(010) # should give 8
print(0o10)	# How to do this in Python 3
print(0xf)	# Hex
print(0b10)	# Binary

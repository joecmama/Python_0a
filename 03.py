#!/usr/bin/env python

# basic string operations

a = 'hello '
b = 'world'
c = a+b
print(c)

print(a == 'hello')
print(a < 'zebra')
print(a > 'zebra')
print(a < 'aardvark')
print(a != 'hello ')
# 
print(c)
print(c.startswith('hello'))
print(c.endswith('world'))
print(len(c)) # length of a string
# 
print('lo wo' in c) # c contains a substring?
print(c.find('lo wo'))
print(c.find('blahbedy'))
print(c.find('o'))
# 
d = c.replace('hello','hi there')
print(c)
print(d)

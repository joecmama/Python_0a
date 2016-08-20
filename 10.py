#!/usr/bin/env python

# for loops
for i in range(0,10):
  print(i)
# 
# # loop over elements in a list
a = ['a','b','c','d','e','f']
for i in a:
  print(i)
# 
# # break and loop else
for i in a:
  if i == 'c':
    print('I found a "c"')
    break
else: # Do this if NOT break
  print('did not find a "c"')

# # continue
for i in a:
  if i =='c':
    continue
  print(i)

# multiple assignment 
a = [['a',1],['b',2],['c',3]]
for i,j in a:
    print('i=%s, j=%d' % (i,j))
    #print(i,j)

# ...and zip ... very useful when traversing multiple parallel lists
a = ['a','b','c','d']
b = [1,2,3]
c = ['h','i','j']
print(zip(a,b,c))
for i,j,k in zip(a,b,c):
    print(i,j,k)
# 
x = [2.643,5.2342,1.23]
y = [0.45,-2.3,0.56]

# print out square distance to origin
from math import sqrt
for ix,iy in zip(x,y):
  print(ix**2+iy**2)

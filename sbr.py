#!/usr/bin/env python

def a(): 
  print('This is a subroutine')
#print('No longer part of the subroutine.')

#a()
#a()
#a()
#
# In C, you would need two functions, 1 for number input, 1 for string input
def b(x,y):
  print('This is a subroutine with two arguments x: ' + str(x)+ ' and y: ' + str(y))
 
b(23,46)
b(['hi','there'],23)

b('hi','there')
b('there','hi')
# vs....
b(x='hi', y='there') # named arguments
b(y='there', x='hi') # named arguments
#
# subroutine with a return value (or function)
def add(x,y):
    return x+y

print(add(1,2))
#
#
b(add(1,2),add('hi','there'))
#
#add(3) # Error


# default arguments
def c(x='defaultX', y='defaultY'):
    print('x = ' + str(x) + ' y = ' + str(y))

c(2,3)
c(4)
c(y='hi')
c()
#c(3,2,1)  # Error

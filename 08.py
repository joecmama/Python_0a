#!/usr/bin/env python

# if statements

a = 37
# simple if statement
if a == 37:  # two equals signs for comparison (one for assignment)
    print('yes, a is equal to 37')

if a != 38: print('no, a is not equal to 38')

# multi line if with indenting
a = 14
if a > 10:
    print('bigger than 10')
    print('yes')
    if a > 20:
      print('really big')
      print('second level')
    print('first level')
print('always') 

# # if-then-else
a = 4
if a > 10:
  print('bigger than 10')
else:
  print('less than or equal to 10\n')

# if-then-else with different branches
a = 27
if a == 5:
    print('smaller than 5')
elif a == 10:
    print('smaller than 10')
elif a == 15:
    print('smaller than 15')
else:
    print('I give up')
# 
# # ternary operator
a = 98
print 40+(2*a if a > 100 else 0.5*a)

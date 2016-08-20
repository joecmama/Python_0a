#!/usr/bin/env python

# exceptions

# a = ['hi','there','everyone']
# #print(a[3]) # produces an IndexError
# 
# try:
#     print(a[3])
#     print('that went OK.')
# except IndexError:
#     print('Nice try.  list element does not exist.')
# print('still chugging along.')
# 
# class MyVeryBadError(Exception): pass
# 
# def do_something_bad(x):
#   b = {'key':'val'}
# #  print(a[3]) # produces an IndexError
# #  print(b['lala']) # produces a KeyError
# #  print(10.0/0.0) # produces ZeroDivisionError
# #  print(10.0**(10.0**100.0)) # what is this number called?
#   if (x > 10):
#       raise MyVeryBadError
#   print('x is OK.')
# 
# #do_something_bad(23)
# 
# try:
#     do_something_bad(23)
# except IndexError:
#     print('sorry, that list element does not exist')
# except KeyError:
#     print('that key does not exist')
# except ZeroDivisionError:
#     print('you are trying to divide by zero.')
# except OverflowError:
#     print('number is too big.')
# except MyVeryBadError:
#     print('oh NOOOOOO!!!')
# 
# print('...but still chugging along')

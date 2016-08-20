#!/usr/bin/env python

# basic math

print(2+3)  # addition
print(2*3)  # multiplication
print(2**3) # exponentiation
# 
# # in python2: / means integer division (truncation) for integers
# # and floating pt division for floating point number
# #
# # in python3: / always means floating point division (like perl)
print(2/3)
print(4/3)
print(2.0/3.0)
# 
# # either python2 or python3: // means integer division
print(7//3)
print(2.0//3.0)
print(5.0 % 2.0) # remainder
# 
# # one equals sign: assignment
a = 37
print(a == 37) # two equals signs: comparison
print(a < 40)
print(a >= 12)
# 
# # chained comparisons
print(36 < a < 38)
print(36 < a < 37)
# 
# # Boolean operators
b = 21
print(a == 37 and b == 20)
print(a == 37 or b == 19)
print(a != 37)
print(not a == 37 )
# 
# # C style assignment operators
a = 11
print(a)
a += 2
print(a)
a += 1
# # no a++ !
print(a)


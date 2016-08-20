#!/usr/bin/env python

# lists - part 1

# # This is a list
a = ['hello','world','my','lucky','number','is', 37]
print(a)
# 
# # Lists are indexed from zero
print(a[0], a[4])
# 
# # Lists have bounds checking
# print a[23]
# 
# # Negative numbers mean from the end
print(a[-1], a[-2])
# 
# # A slice is a range, from first index (included) to last index (excluded)
print(a[1:3])
print(a[2:-2])
print(a[4:])
print(a[:5])
# Return the whole array
print(a[:])
print(a)
print(a[0:7])
print(a[0:len(a)])
# 
# # Lists can be created with a range
print(list(range(23)))     # 0 through 22 
print(list(range(1,10)))   # 1 through 9 
print(list(range(0,30,5)))   # 0 through 30 by 5's

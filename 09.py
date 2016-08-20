#!/usr/bin/env python

# while loops

a = 10
while a <= 100000:
    a *= 10
    print(a)
print('this is no longer in the loop because not indented')
# 
a = 10
while a > 0:
    print(a)
    if a == 5: 
      break
    a -= 1

a = 10
while a > 0:
    a -= 1
    if a % 2 == 0: 
        continue # skip if a is even
    print(a)
# 
print('---')
# a = 0 
a = 5
while a > 3:
    if a == 2: 
        break
    print(a)
    a -= 1
else:
    print('made it to the end')


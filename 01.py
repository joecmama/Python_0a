#!/usr/bin/env python

'''
Long multi-line comment
'''

# # anything after a # is ignored - used for comments
# 
# # basic objects in python: numbers...
print(23)        # integer
print(2.141)     # floating point
# 
# # ...and strings
print('hi there')
print("hi there")
print('I like to say "hi"')
print("I like to say 'hi'")
print("I like to say \"hi\"")
print('''a big multiline string

can look like this.

hi there how are you''')
# 
# # a backslash codes special characters
print('Special codes: newline\nand tab\ttab\ttab')
# 
# # raw string to ignore backslashes
print(r'what you see is what you get\n\t\t\n')
# 
# # strings and numbers are different things
print(23+46) # addition
print('23'+'46') # string concatenation
# 
# # but they can be interconverted
print(23 + int('46'))
print(str(23) + str(46))
print('hi there ' + str(3 + float('4.556')))

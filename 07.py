#!/usr/bin/env python

# dictionaries

# # A dictionary is a set of (unordered) key-value pairs (often keys are strings)
d = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(d)
print(d['key1'])
# 
# # Trying to retrieve a value for a key that doesn't exist gives an error
# #print(d['notthere'])
# 
# # Values can be lists or dictionaries themselves
fancy = {'key1': [1,2,3], 'key4': 'hiya', 'key2': {'subkey1': 'hi', 'subkey2': 'there'}}
print(fancy)
print(fancy['key2'])
print(fancy['key2']['subkey1'])
# #
# # You can get a list of keys
print(d.keys())
print(fancy.keys())
# 
# # ... or of values
print(fancy.values())
# 
# # You can add more items
print(fancy)
fancy['key5'] = 'something else'
print(fancy)
# 
# ## ... or delete them
del fancy['key1']
print(fancy)
# 
# # dictionary comprehension - like a list comprehension
d = {s: len(s) for s in ['hi','there','everyone']}
print(d)

d = {s: len(s) for s in ['hi','there','everyone'] if s.startswith('h')}
print(d)

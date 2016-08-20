#!/usr/bin/env python

import json

table = [ {'key1': [1,2,3], 'key2':'there', 
           'key3':{'subkey1':['a','b','c'], 'subkey2':['d','e','f']}}, 45, 78]
print(table)

with open('out.json','w') as f:
    json.dump(table, f, sort_keys=True, indent=2)

with open('in.json') as f:
     tab = json.load(f)
     print(tab[0])
     print(tab[1])
     print(tab[0]['field1'][1])

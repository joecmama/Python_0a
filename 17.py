#!/usr/bin/env python

# object persistence	# So variables and values are stored after session, 'persistently.'

import shelve

# Define filename:
fname='tmp.db'

def store_data():
   db = shelve.open(fname)
   db['key1'] = 'here is some data'
   db['another key'] = ['some','more','data']
   db.close()

def add_some_more_data():
   db = shelve.open(fname)
   db['more data'] = [[12,13,14],[67,67,89]]
   db.close()

def show_data():
   db = shelve.open(fname)
   print(db)
   db.close()

#store_data()
add_some_more_data()
show_data()


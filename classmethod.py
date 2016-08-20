#!/usr/bin/env python

class A:

    def __init__(self, d):
        self.data = d

    def show_data(self): # no decorator: instance method
        print(self.data)

    @classmethod # decorator to say it's a class method
    def show_class(self_class):
        print(self_class.__name__)

a = A('hi')
b = A('different data')
print(dir(A))

## instance method
a.show_data()
b.show_data()

## class method
#A.show_class()
a.show_class()
b.show_class()

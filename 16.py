#!/usr/bin/env python

# classes

class A:
    def __init__(self, d=100):
        self.data = d
    def show_data(self):
        #print('here is my data: ' + self.data)
        print('here is my data: ' + str(self.data))
# 
a = A('hi there') # created an object of class A with data 'hi there'
b = A('more data')
c = A('some more')
d = A([1,2,23,4,43])
e = A()

a.show_data()
b.show_data()
c.show_data()
d.show_data()
e.show_data()

# 
# a2 = A('oh') # another object of class A with data 'oh'
# a2.show_data()
# a2.data = 'something else'
# a2.show_data()
# 
# # B is a subclass, which "inherits" from A
# class B(A):
#     def __init__(self, d, d2):
#         A.__init__(self, d)
#         self.data2 = d2
#     def show_both(self):
#         print('data: ' + self.data + ', data2: ' + self.data2)
# 
# b = B('HI', 'THERE')
# b.show_data()
# b.show_both()
# 
# importing a user-defined module
from v3 import V3, distance
a = V3(1,2,3)
b = V3(5,6,7)
print(distance(a,b))
print(a+b)

c = V3(1,2,3)
d = V3(5,6,7)
print(distance(c,d))
print(c+d)


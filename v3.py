from math import sqrt,acos

class V3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(a, b): return V3(a.x+b.x, a.y+b.y, a.z+b.z)
    def __sub__(a, b): return V3(a.x-b.x, a.y-b.y, a.z-b.z)
    def __repr__(self): return `self.x,self.y,self.z`
    def sq(self): return dot(self,self)
    def norm(self): return sqrt(self.sq())
    def scaled_by(self, a): return V3(a*self.x, a*self.y, a*self.z)
    def as_unit(self): return self.scaled_by(1.0/self.norm())
    def ident(self): return self

def dot(a, b): return a.x*b.x + a.y*b.y + a.z*b.z
def distance2(a, b): return (a-b).sq()
def distance(a, b): return sqrt(distance2(a,b))

def angle(a, b, c):
    t = dot((a-b).as_unit(), (c-b).as_unit())
    if (t > 1):
        t = 1
    elif (t < -1):
        t = -1
    return acos(t)

from math import *
class Grad:
    def __init__(self,value,_children={}):
        self.value = value
        
        self._children = set(_children)
        print(self._children)
    def __add__(self,other):
        print(self.value + other.value)
        return Grad(self.value + other.value, {other.value,self.value})
    def __sub__(self,other):
        print(self.value - other.value)
        return Grad(self.value - other.value)
    def __mul__(self,other):
        print(self.value * other.value)
        return Grad(self.value * other.value)
    def g(self):
        print(1/1+exp(-self.value))
        return Grad(1/1+exp(-self.value))
    def backward(self):
        print("backward",self)
        

# z = wx+b
# a = g(z)


w = Grad(10)
x = Grad(25)
b = Grad(2)
z1 = w + x
z = z1 + b
# a = z.g()

# dzdz = 1
# dzdz1 = 

print("--------------------------")

# Manual back prop
h = 0.01
w1 = Grad(10)
x1 = Grad(25)
b1 = Grad(2)
z2 = w1 + x1
z2 = z2.value + h
z3 = z2 + b.value
z3 = z3

print(f"dz/dz1:{(z3-z.value)/h}")

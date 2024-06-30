from math import *
class Grad:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        print(self.value + other.value)
        return Grad(self.value + other.value)
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
a = z.g()
a.backward()
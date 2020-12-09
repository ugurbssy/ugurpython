class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

class Triangle(Shape):

    def __init__(self, min, med, max):
        super().__init__()
        self.min = min
        self.med = med
        self.max = max

    def perimeter_cal(self):
        return (self.min + self.med + self.max)

    def __repr__(self):
        return self.__class__.__name__ + "[min=" + str(self.min) + "med=" + str(self.med) + "max=" + str(self.max) +"] at " + str(hex(id(self)))

class EquilTriangle(Shape):

    def __init__(self, length):
        super().__init__()
        self.length=length

    def perimeter_cal(self):
        return (self.length* 3)

    def __repr__(self):
        return self.__class__.__name__ + "[length=" + str(self.length)  +"] at " + str(hex(id(self)))

class Square(Rectangle):

    def calc_surface(self):
        return self._a**2
    def __repr__(self):
        return self.__class__.__name__ + "[length=" + str(self._a)  +"] at " + str(hex(id(self)))


r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
print(c.calc_surface())

u= Triangle(3,4,5)
print(u)
print(u.perimeter_cal())

e= EquilTriangle(7)
print(e)
print(e.perimeter_cal())

s = Square(5)
print(s)
print(s.calc_surface())


import math


class circ:
    pi = math.pi

    def __init__(self, r):
        self.rad = r

    def area(self):
        area = (self.rad)**2 * (self.pi)
        return area

    def peri(self):
        perim = 2*self.pi*self.rad
        return perim


c1 = circ(5)
c1.area()
c1.peri()
print("Area of the circle:", c1)

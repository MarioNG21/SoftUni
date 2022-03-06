import math


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


class Triangle:
    def __init__(self, side, height):
        self.height = height
        self.side = side

    def area(self):
        return self.side * self.height / 2


class Square(Rect):
    def __init__(self, side):
        super().__init__(side, side)

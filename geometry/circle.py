import math
from .shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return round(math.pi * self.radius**2, 3)

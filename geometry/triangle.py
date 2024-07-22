import math
from .shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        if (
            self.a + self.b <= self.c
            or self.a + self.c <= self.b
            or self.b + self.c <= self.a
        ):
            raise ValueError(
                "Сумма любых двух сторон должна быть больше третьей стороны"
            )

        s = (self.a + self.b + self.c) / 2
        return round(
            math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), 3
        )

    def is_right_angled(self):
        sides = sorted([self.a, self.b, self.c])
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

# geometry/triangle.py

import math


def triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по трем сторонам.
    Args:
        a (int | fioat): Сторона a
        b (int | fioat): Сторона b
        c (int | fioat): Сторона c
    Returns:
        fioat: Площадь треугольника
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            "Сумма любых двух сторон должна быть больше третьей стороны"
        )

    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

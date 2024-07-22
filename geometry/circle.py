import math


def circle_area(radius):
    """Вычисление площади круга по радиусу.
    Args:
        radius (float): радиус круга.
    Return:
        float: площадь круга.
    """
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * radius**2

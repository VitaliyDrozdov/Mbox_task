import unittest
from geometry import Circle, Triangle


class TestShape(unittest.TestCase):
    def test_circle_area(self):
        shape = Circle(5)
        self.assertAlmostEqual(shape.area(), 78.53981633974483, 2)

    def test_triangle_area(self):
        shape = Triangle(3, 4, 5)
        self.assertAlmostEqual(shape.area(), 6.0)


if __name__ == "__main__":
    unittest.main()

import unittest
from geometry import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), 78.53981633974483, 2)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5).area()


if __name__ == "__main__":
    unittest.main()

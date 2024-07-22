import unittest
from geometry import Triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3).area()

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5).area()

    def test_is_right_angled(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right_angled())

    def test_is_not_right_angled(self):
        t = Triangle(3, 4, 6)
        self.assertFalse(t.is_right_angled())


if __name__ == "__main__":
    unittest.main()

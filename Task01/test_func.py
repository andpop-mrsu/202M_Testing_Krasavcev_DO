import unittest

from triangle_func import IncorrectTriangleSides, get_triangle_type


class TestGetTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(10, 10, 10), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(5, 8, 5), 'isosceles')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(12, 9, 6), 'nonequilateral')

    def test_negative_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, -4, 5)

    def test_impossible_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 2, 10)

    def test_zero_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 9, 9)


if __name__ == '__main__':
    unittest.main()
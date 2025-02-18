import pytest

from triangle_class import IncorrectTriangleSides, Triangle


def test_triangle_creation():
    triangle = Triangle(12, 9, 6)
    assert triangle.side_a == 12
    assert triangle.side_b == 9
    assert triangle.side_c == 6


def test_triangle_type_equilateral():
    triangle = Triangle(10, 10, 10)
    assert triangle.triangle_type() == "equilateral"


def test_triangle_type_isosceles():
    triangle = Triangle(5, 8, 5)
    assert triangle.triangle_type() == "isosceles"


def test_triangle_type_nonequilateral():
    triangle = Triangle(12, 9, 6)
    assert triangle.triangle_type() == "nonequilateral"


def test_triangle_creation_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(5, -4, 5)


def test_triangle_creation_impossible_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 2, 10)


def test_triangle_creation_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 9, 9)


def test_triangle_perimeter():
    triangle = Triangle(12, 9, 6)
    assert triangle.perimeter() == 23


def test_triangle_perimeter_equilateral():
    triangle = Triangle(10, 10, 10)
    assert triangle.perimeter() == 30
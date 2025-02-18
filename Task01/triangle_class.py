class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if not (side_a + side_b > side_c) or not (side_a + side_c > side_b) or not (side_b + side_c > side_a):
            raise IncorrectTriangleSides("Incorrect side lengths of a triangle")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def triangle_type(self):
        if self.side_a == self.side_b == self.side_c:
            return "equilateral"
        elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
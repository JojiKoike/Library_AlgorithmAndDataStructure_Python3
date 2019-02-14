import unittest

from geometry.structs import Point, Vector, Segment
from geometry.methods import is_orthogonal


class GeometryMethodTestCase(unittest.TestCase):
    def test_is_orthogonal_vector_normal(self):
        # Vector
        v_1: Vector = Vector(1.0, 1.0)
        v_2: Vector = Vector(1.0, -1.0)
        self.assertEqual(is_orthogonal(v_1, v_2), True)
        # Points
        p_1: Point = Point(1.0, 1.0)
        p_2: Point = Point(2.0, 2.0)
        p_3: Point = Point(1.0, -1.0)
        p_4: Point = Point(2.0, -2.0)
        self.assertEqual(is_orthogonal(p_1, p_2, p_3, p_4), True)
        # Segments
        s_1: Segment = Segment(p_1, p_2)
        s_2: Segment = Segment(p_3, p_4)
        self.assertEqual(is_orthogonal(s_1, s_2), True)


if __name__ == '__main__':
    unittest.main()

import unittest

from geometry.structs import Point, Vector, Segment
from geometry.methods import is_orthogonal, is_parallel, project, reflect
from geometry.common import equals


class GeometryMethodTestCase(unittest.TestCase):
    def test_is_orthogonal_normal(self):
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

    def test_is_parallel_normal(self):
        # Vector
        v_1: Vector = Vector(1.0, 1.0)
        v_2: Vector = Vector(2.0, 2.0)
        self.assertEqual(is_parallel(v_1, v_2), True)
        # Points
        p_1: Point = Point(1.0, 1.0)
        p_2: Point = Point(2.0, 2.0)
        p_3: Point = Point(-1.0, -1.0)
        p_4: Point = Point(-2.0, -2.0)
        self.assertEqual(is_parallel(p_1, p_2, p_3, p_4), True)
        # Segments
        s_1: Segment = Segment(p_1, p_2)
        s_2: Segment = Segment(p_3, p_4)
        self.assertEqual(is_parallel(s_1, s_2), True)

    def test_project_normal(self):
        seg: Segment = Segment(Point(0, 0), Point(3, 4))
        p: Point = Point(2, 5)
        self.assertEqual(equals(project(seg, p).x, 3.12), True)
        self.assertEqual(equals(project(seg, p).y, 4.16), True)

    def test_reflect_normal(self):
        seg: Segment = Segment(Point(0, 0), Point(3, 4))
        p: Point = Point(2, 5)
        self.assertEqual(equals(reflect(seg, p).x, 4.24), True)
        self.assertEqual(equals(reflect(seg, p).y, 3.32), True)


if __name__ == '__main__':
    unittest.main()

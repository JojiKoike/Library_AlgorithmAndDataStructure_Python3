import unittest
import math
from geometry.structs import Point, Vector, Segment, Line
from geometry.methods import \
    is_orthogonal, is_parallel, project, reflect, \
    get_distance, get_distance_lp, get_distance_sp, \
    get_point_relative_position, intersect
from geometry.common import equals, PointRelativePosition


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

    def test_get_distance_normal(self):
        p_1: Point = Point(0, 0)
        p_2: Point = Point(1, 1)
        self.assertEqual(equals(get_distance(p_1, p_2), math.sqrt(2.0)), True)

    def test_get_distance_lp_normal(self):
        l: Line = Line(Point(0, 0), Point(1, 1))
        p: Point = Point(0.5, 0)
        self.assertEqual(equals(get_distance_lp(l, p), 0.5 / math.sqrt(2)), True)

    def test_get_distance_sp_normal(self):
        p_l: Point = Point(-1, -1)
        p_r: Point = Point(1, 1)
        s: Segment = Segment(p_l, p_r)
        p_1: Point = Point(-2, -2)
        p_2: Point = Point(0, 1)
        p_3: Point = Point(2, 2)
        self.assertEqual(equals(get_distance_sp(s, p_1), (p_1 - p_l).abs()), True)
        self.assertEqual(equals(get_distance_sp(s, p_2), 1.0 / math.sqrt(2)), True)
        self.assertEqual(equals(get_distance_sp(s, p_3), (p_3 - p_r).abs()), True)

    def test_get_point_relative_position_normal(self):
        p_0: Point = Point(0, 0)
        p_1: Point = Point(2, 0)
        self.assertEqual(
            get_point_relative_position(p_0, p_1, Point(-1, 1)),
            PointRelativePosition.COUNTER_CLOCK_WISE)
        self.assertEqual(
            get_point_relative_position(p_0, p_1, Point(-1, -1)),
            PointRelativePosition.CLOCK_WISE
        )
        self.assertEqual(
            get_point_relative_position(p_0, p_1, Point(-1, 0)),
            PointRelativePosition.ON_LINE_BACK
        )
        self.assertEqual(
            get_point_relative_position(p_0, p_1, Point(3, 0)),
            PointRelativePosition.ON_LINE_FRONT
        )
        self.assertEqual(
            get_point_relative_position(p_0, p_1, Point(1, 0)),
            PointRelativePosition.ON_SEGMENT
        )

    def test_intersect_normal(self):
        s_1: Segment = Segment(Point(0, 0), Point(3, 0))
        s_2: Segment = Segment(Point(1, 1), Point(2, -1))
        s_3: Segment = Segment(Point(3, 1), Point(3, -1))
        s_4: Segment = Segment(Point(3, -2), Point(5, 0))
        self.assertEqual(intersect(s_1, s_2), True)
        self.assertEqual(intersect(s_1, s_3), True)
        self.assertEqual(intersect(s_1, s_4), False)


if __name__ == '__main__':
    unittest.main()

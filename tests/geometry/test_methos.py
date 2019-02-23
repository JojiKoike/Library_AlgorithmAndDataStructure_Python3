"""
Geometry Methods Test Module
"""
import unittest
import math
from typing import List
from geometry.structs import Point, Vector, Segment, Line, Circle, Polygon
from geometry.methods import \
    is_orthogonal, is_parallel, project, reflect, \
    get_distance, get_distance_lp, get_distance_sp, \
    get_point_relative_position, intersect, get_distance_ss, get_cross_point, \
    get_cross_points_circle_and_line, get_common_points_circle_and_circle, \
    point_contained_in_polygon, get_convex_hull, get_num_of_segment_intersections
from geometry.common import equals, PointRelativePosition, PointContainsInPolygon


class GeometryMethodTestCase(unittest.TestCase):
    """
    Geometry Methods Test Case Class
    """
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

    def test_get_distance_ss_normal(self):
        s_0: Segment = Segment(Point(0, 0), Point(2, 2))
        s_1: Segment = Segment(Point(-3, -3), Point(-1, -1))
        s_2: Segment = Segment(Point(0, -3), Point(1, -2))
        s_3: Segment = Segment(Point(0, 2), Point(2, 0))
        self.assertEqual(equals(get_distance_ss(s_0, s_1), math.sqrt(2)), True)
        self.assertEqual(equals(get_distance_ss(s_0, s_2), math.sqrt(5)), True)
        self.assertEqual(equals(get_distance_ss(s_0, s_3), 0), True)

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

    def test_get_cross_point_normal(self):
        s_1: Segment = Segment(Point(0, 0), Point(1, 1))
        s_2: Segment = Segment(Point(0, 1), Point(1, 0))
        s_3: Segment = Segment(Point(1, 0), Point(0, 1))
        s_4: Segment = Segment(Point(0, 1), Point(1, 2))
        self.assertEqual(equals(get_cross_point(s_1, s_2).x, 0.5), True)
        self.assertEqual(equals(get_cross_point(s_1, s_2).y, 0.5), True)
        self.assertEqual(equals(get_cross_point(s_1, s_3).x, 0.5), True)
        self.assertEqual(equals(get_cross_point(s_1, s_3).y, 0.5), True)
        self.assertIsNone(get_cross_point(s_1, s_4))

    def test_get_cross_point_line_and_circle(self):
        c_0: Circle = Circle(Point(1, 1), 2)
        l_1: Line = Line(Point(0, -2), Point(1, -2))
        l_2: Line = Line(Point(0, -1), Point(1, -1))
        l_3: Line = Line(Point(0, 0), Point(1, 0))
        self.assertIsNone(get_cross_points_circle_and_line(c_0, l_1))
        self.assertEqual(len(get_cross_points_circle_and_line(c_0, l_2)), 1)
        self.assertTrue(equals(get_cross_points_circle_and_line(c_0, l_2)[0].x, 1.0))
        self.assertTrue(equals(get_cross_points_circle_and_line(c_0, l_2)[0].y, -1.0))
        self.assertEqual(len(get_cross_points_circle_and_line(c_0, l_3)), 2)
        self.assertTrue(equals(get_cross_points_circle_and_line(c_0, l_3)[0].x, 1 + math.sqrt(3)))
        self.assertTrue(equals(get_cross_points_circle_and_line(c_0, l_3)[1].x, 1 - math.sqrt(3)))

    def test_get_common_points_circle_and_circle_normal(self):
        c_1: Circle = Circle(Point(0, 0), 2.0)
        c_2: Circle = Circle(Point(2.0, 0), 2.0)
        # Intersects Case
        res: List[Point] = get_common_points_circle_and_circle(c_1, c_2)
        self.assertEqual(len(res), 2)
        self.assertTrue(equals(res[0].x, 2.0 * 1.0 / 2.0))
        self.assertTrue(equals(res[0].y, 2.0 * math.sqrt(3.0) / 2.0))
        self.assertTrue(equals(res[1].x, 2.0 * 1.0 / 2.0))
        self.assertTrue(equals(res[1].y, -2.0 * math.sqrt(3.0) / 2.0))
        c_2_1: Circle = Circle(Point(0, 2.0), 2.0)
        res = get_common_points_circle_and_circle(c_1, c_2_1)
        self.assertEqual(len(res), 2)
        self.assertTrue(equals(res[0].x, -2.0 * math.sqrt(3.0) / 2.0))
        self.assertTrue(equals(res[0].y, 2.0 * 1.0 / 2.0))
        self.assertTrue(equals(res[1].x, 2.0 * math.sqrt(3.0) / 2.0))
        self.assertTrue(equals(res[1].y, 2.0 * 1.0 / 2.0))
        c_2_2: Circle = Circle(Point(2.0, 2.0), 2.0)
        res = get_common_points_circle_and_circle(c_1, c_2_2)
        self.assertEqual(len(res), 2)
        self.assertTrue(equals(res[0].x, 0))
        self.assertTrue(equals(res[0].y, 2.0))
        self.assertTrue(equals(res[1].x, 2.0))
        self.assertTrue(equals(res[1].y, 0))
        # Contacts Case
        c_3: Circle = Circle(Point(4.0, 0), 2.0)
        res = get_common_points_circle_and_circle(c_1, c_3)
        self.assertEqual(len(res), 1)
        self.assertTrue(equals(res[0].x, 2.0))
        self.assertTrue(equals(res[0].y, 0))
        # Not Intersects and Contacts Case
        c_4: Circle = Circle(Point(5.0, 0), 2.0)
        res = get_common_points_circle_and_circle(c_1, c_4)
        self.assertIsNone(res)
        c_5: Circle = Circle(Point(1.0, 0), 0.5)
        res = get_common_points_circle_and_circle(c_1, c_5)
        self.assertIsNone(res)
        # Completely Duplicates Case
        res = get_common_points_circle_and_circle(c_1, c_1)
        self.assertIsNone(res)

    def test_point_contained_in_polygon(self):
        poly: Polygon = Polygon([Point(0, 0), Point(3, 1), Point(2, 3), Point(0, 3)])
        p_1: Point = Point(2, 1)
        self.assertEqual(point_contained_in_polygon(poly, p_1), PointContainsInPolygon.IN)
        p_2: Point = Point(0, 2)
        self.assertEqual(point_contained_in_polygon(poly, p_2), PointContainsInPolygon.ON_EDGE)
        p_3: Point = Point(3, 2)
        self.assertEqual(point_contained_in_polygon(poly, p_3), PointContainsInPolygon.OUT)

    def test_get_convex_hull_normal(self):
        poly: Polygon = Polygon([Point(2, 1), Point(0, 0), Point(1, 2),
                                 Point(2, 2), Point(4, 2), Point(1, 3), Point(3, 3)])
        res: Polygon = get_convex_hull(poly)
        self.assertEqual(5, len(res.p_i))
        x_expected: List[float] = [0, 2, 4, 3, 1]
        y_expected: List[float] = [0, 1, 2, 3, 3]
        for i in range(5):
            self.assertTrue(equals(res.p_i[i].x, x_expected[i]))
            self.assertTrue(equals(res.p_i[i].y, y_expected[i]))

    def test_get_num_of_segment_intersections_normal(self):
        segments: List[Segment] = [Segment(Point(2, 2), Point(2, 5)),
                                   Segment(Point(1, 3), Point(5, 3)),
                                   Segment(Point(4, 1), Point(4, 4)),
                                   Segment(Point(5, 2), Point(7, 2)),
                                   Segment(Point(6, 1), Point(6, 3)),
                                   Segment(Point(6, 5), Point(6, 7))]
        self.assertEqual(3, get_num_of_segment_intersections(segments))


if __name__ == '__main__':
    unittest.main()

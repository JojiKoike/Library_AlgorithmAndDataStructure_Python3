"""
Geometry Data Structure Definition Tests Module
"""
import unittest
from geometry.structs import Point, Segment, Circle


class GeometryStructsTestCase(unittest.TestCase):
    """
    Geometry Data Structure Test Case Class
    """
    def test_defined_point_correctly(self) -> None:
        """
        Point Data Structure Normal Case Test
        :return: None
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                point: Point = Point(i * 1.0, j * 1.0)
                self.assertEqual(point.x, i * 1.0)
                self.assertEqual(point.y, j * 1.0)

    def test_defined_segment_correctly(self) -> None:
        """
        Segment Data Structure Normal Case Test
        :return: None
        """
        segment: Segment = Segment(Point(0.1, 0.2), Point(0.3, 0.4))
        self.assertEqual(segment.p1.x, 0.1)
        self.assertEqual(segment.p1.y, 0.2)
        self.assertEqual(segment.p2.x, 0.3)
        self.assertEqual(segment.p2.y, 0.4)

    def test_defined_circle_correctly(self) -> None:
        """
        Circle Data Structure Normal Case Test
        :return: None
        """
        circle: Circle = Circle(Point(0.5, 0.7), 3.5)
        self.assertEqual(circle.c.x, 0.5)
        self.assertEqual(circle.c.y, 0.7)
        self.assertEqual(circle.r, 3.5)


if __name__ == '__main__':
    unittest.main()

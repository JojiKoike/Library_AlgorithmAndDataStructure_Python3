"""
Geometry Data Structure Definition Tests Module
"""
import unittest
from geometry.structs import Point


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


if __name__ == '__main__':
    unittest.main()

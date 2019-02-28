"""
Data Structure Structs Test Module
"""
import unittest
from typing import List
from datastructure.structs import DisjointSet, Point


class DataStructureStrutsTestCase(unittest.TestCase):
    """
    DataStructure Structs Test Case Class
    """
    def test_disjoint_set_normal(self):
        ds: DisjointSet = DisjointSet(5)
        ds.unite(1, 4)
        ds.unite(2, 3)
        self.assertFalse(ds.same(1, 2))
        self.assertFalse(ds.same(3, 4))
        self.assertTrue(ds.same(1, 4))
        self.assertTrue(ds.same(3, 2))
        ds.unite(1, 3)
        self.assertTrue(ds.same(2, 4))
        self.assertFalse(ds.same(3, 0))
        ds.unite(0, 4)
        self.assertTrue(ds.same(0, 2))
        self.assertTrue(ds.same(3, 0))

    def test_point_normal(self):
        points: List[Point] = [Point(i, i + 1, i + 2) for i in range(5)]
        sorted(points, reverse=True)
        for i in range(4, -1, -1):
            self.assertEqual(points[i].point_id, i)
            self.assertEqual(points[i].x, i + 1)
            self.assertEqual(points[i].y, i + 2)
            print(points[i])


if __name__ == '__main__':
    unittest.main()

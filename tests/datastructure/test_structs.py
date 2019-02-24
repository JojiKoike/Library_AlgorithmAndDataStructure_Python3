"""
Data Structure Structs Test Module
"""
import unittest
from datastructure.structs import DisjointSet


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


if __name__ == '__main__':
    unittest.main()

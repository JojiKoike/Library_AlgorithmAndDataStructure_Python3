import unittest
from typing import List
from datastructure.structs import Node, Point
from datastructure.methods import make_kd_tree, find_range_search


class DataStructureMethodsTestCase(unittest.TestCase):

    def test_make_kd_tree_normal(self):
        points: List[Point] = [
            Point(0, 2, 1), Point(1, 2, 2), Point(2, 4, 2),
            Point(3, 6, 2), Point(4, 3, 3), Point(5, 5, 4)
        ]
        tree: List[Node] = [Node(None, None, None, None) for i in range(6)]
        t: int = make_kd_tree(0, 6, 0, points, tree, 0)
        self.assertEqual(0, t)


if __name__ == '__main__':
    unittest.main()

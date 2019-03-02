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
        t: int = make_kd_tree(0, 6, 0, points, tree)
        for node in tree:
            print("[{0},{1},{2},{3}]".format(
                node.location, node.p, node.l, node.r))

        self.assertEqual(0, t)

    def test_find_range_search_normal(self):
        points: List[Point] = [
            Point(0, 2, 1), Point(1, 2, 2), Point(2, 4, 2),
            Point(3, 6, 2), Point(4, 3, 3), Point(5, 5, 4)
        ]
        tree: List[Node] = [Node(None, None, None, None) for i in range(6)]
        t: int = make_kd_tree(0, 6, 0, points, tree)
        ans1: List[Point] = []
        find_range_search(t, 2, 4, 0, 4, 0, points, tree, ans1)
        ans1.sort()
        for i, id in enumerate([0, 1, 2, 4]):
            self.assertEqual(id, ans1[i].point_id)
        ans2: List[Point] = []
        find_range_search(t, 4, 10, 2, 5, 0, points, tree, ans2)
        ans2.sort()
        for i, id in enumerate([2, 3, 5]):
            self.assertEqual(id, ans2[i].point_id)


if __name__ == '__main__':
    unittest.main()

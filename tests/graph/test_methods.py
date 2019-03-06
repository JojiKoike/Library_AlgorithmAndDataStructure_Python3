import unittest
from typing import List
from graph.common import INFINITY
from graph.methods import warshall_floyd, topological_sort, articulation_point


class GraphMethodsTestCase(unittest.TestCase):

    def test_warshall_floyd_normal(self):
        dt: List[List[int]] = [[0 if j == i else INFINITY for j in range(4)] for i in range(4)]
        dt[0][1] = 1
        dt[0][2] = 5
        dt[1][2] = 2
        dt[1][3] = 4
        dt[2][3] = 1
        dt[3][2] = 7
        res: List[List[int]] = warshall_floyd(dt)
        expect: List[List[int]] \
            = [[0, 1, 3, 4], [INFINITY, 0, 2, 3], [INFINITY, INFINITY, 0, 1], [INFINITY, INFINITY, 7, 0]]
        for i in range(4):
            for j in range(4):
                self.assertEqual(expect[i][j], res[i][j])

    def test_warshall_floyd_negative_roop(self):
        dt: List[List[int]] = [[0 if j == i else INFINITY for j in range(4)] for i in range(4)]
        dt[0][1] = 1
        dt[0][2] = 5
        dt[1][2] = 2
        dt[1][3] = 4
        dt[2][3] = 1
        dt[3][2] = -7
        res: List[List[int]] = warshall_floyd(dt)
        self.assertIsNone(res)

    def test_topological_sort_normal(self):
        adj_table: List[List] = [[1], [2], [], [1, 4], [5], [2]]
        res: List[int] = topological_sort(adj_table)
        for i, id in enumerate([0, 3, 1, 4, 5, 2]):
            self.assertEqual(res[i], id)

    def test_articulation_point_normal(self):
        graph: List[List[int]] = [[1, 2], [0, 2], [0, 3], [2]]
        res: List[int] = articulation_point(graph)
        self.assertEqual(1, len(res))
        self.assertEqual(2, res[0])


if __name__ == '__main__':
    unittest.main()

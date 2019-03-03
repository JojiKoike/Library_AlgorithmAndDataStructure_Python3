import unittest
from typing import List
from graph.common import INFINITY
from graph.methods import warshall_floyd


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





if __name__ == '__main__':
    unittest.main()

import unittest
from graph.structs import Edge
from typing import List


class GraphStructsTestCase(unittest.TestCase):
    def test_edge_normal(self):
        edges: List[Edge] = [Edge(0, 1, 3), Edge(1, 2, 1), Edge(2, 3, 4)]
        edges.sort()
        expects: List[List[int]] = [[1, 2, 1], [0, 1, 3], [2, 3, 4]]
        for i, edge in enumerate(edges):
            self.assertEqual(expects[i][0], edge.source)
            self.assertEqual(expects[i][1], edge.destination)
            self.assertEqual(expects[i][2], edge.weight)


if __name__ == '__main__':
    unittest.main()

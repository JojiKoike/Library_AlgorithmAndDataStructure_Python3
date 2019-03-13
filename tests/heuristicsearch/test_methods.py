import unittest
from typing import List
from heuristicsearch.structs import Queen
from heuristicsearch.methods import eight_queen_solver


class HeuristicSearchMethodTestCase(unittest.TestCase):
    def test_eight_queen_solver_normal(self):
        queens: List[Queen] = [Queen(2, 2), Queen(5, 3)]
        res: List[List[str]] = eight_queen_solver(queens)
        self.assertEqual(8, len(res))
        self.assertEqual(8, len(res[0]))


if __name__ == '__main__':
    unittest.main()

import unittest
from typing import List
from heuristicsearch.structs import Queen
from heuristicsearch.methods import eight_queen_solver, eight_puzzle_solver


class HeuristicSearchMethodTestCase(unittest.TestCase):
    def test_eight_queen_solver_normal(self):
        queens: List[Queen] = [Queen(2, 2), Queen(5, 3)]
        res: List[List[str]] = eight_queen_solver(queens)
        self.assertEqual(8, len(res))
        self.assertEqual(8, len(res[0]))

    def test_eight_puzzle_solver_normal(self):
        data: List[int] = [1, 3, 0, 4, 2, 5, 7, 8, 6]
        res: int = eight_puzzle_solver(data)
        self.assertEqual(4, res)


if __name__ == '__main__':
    unittest.main()

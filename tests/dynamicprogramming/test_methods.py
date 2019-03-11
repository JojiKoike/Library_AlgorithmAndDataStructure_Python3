import unittest
from typing import List
from dynamicprogramming.methods import coin_changing_problem,\
    zero_one_knapsack_problem, lis
from dynamicprogramming.structs import Item


class DynamicProgrammingTestCase(unittest.TestCase):
    """
    Dynamic Programming Test Case Class
    """
    def test_coin_changing_problem(self):
        coins: List[int] = [1, 2, 7, 8, 12, 50]
        res: int = coin_changing_problem(coins, 15)
        self.assertEqual(2, res)

    def test_zero_one_knapsack_problem_normal(self):
        weight: int = 5
        items: List[Item] = [Item(4, 2), Item(5, 2),
                             Item(2, 1), Item(8, 3)]
        max_value: int
        selections: List[int]
        max_value, selections = zero_one_knapsack_problem(items, weight)
        self.assertEqual(13, max_value)
        selections_expects: List[int] = [2, 4]
        for i, selections_expect in enumerate(selections_expects):
            self.assertEqual(selections_expect, selections[i])

    def test_lis_normal(self):
        self.assertEqual(3, lis([5, 1, 3, 2, 4]))


if __name__ == '__main__':
    unittest.main()

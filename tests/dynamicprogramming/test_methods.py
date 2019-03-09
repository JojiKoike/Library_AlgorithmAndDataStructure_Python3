import unittest
from typing import List
from dynamicprogramming.methods import coin_changing_problem


class DynamicProgrammingTestCase(unittest.TestCase):
    """
    Dynamic Programming Test Case Class
    """
    def test_coin_changing_problem(self):
        coins: List[int] = [1, 2, 7, 8, 12, 50]
        res: int = coin_changing_problem(coins, 15)
        self.assertEqual(2, res)


if __name__ == '__main__':
    unittest.main()

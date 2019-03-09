"""
Dynamic Programming Method Module
"""
from typing import List
from .common import INFINITY


def coin_changing_problem(coins: List[int], n: int) -> int:
    """
    Coin Changing Problem Solver
    :param coins: Coin List
    :param n: Total payment amount
    :return: Num. of coins payed
    """
    t: List[int] = [INFINITY for i in range(n + 1)]
    t[0] = 0
    for coin in coins:
        j: int = 0
        while coin + j <= n:
            t[coin + j] = min(t[coin + j], t[j] + 1)
            j += 1
    return t[n]

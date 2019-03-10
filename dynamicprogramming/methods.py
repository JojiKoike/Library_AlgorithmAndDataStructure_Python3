"""
Dynamic Programming Method Module
"""
from typing import List, Optional, Tuple, Deque
from collections import deque
from .common import INFINITY, DIAGONAL, TOP
from .structs import Item


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


def zero_one_knapsack_problem(items: List[Item], weight: int) -> Tuple[int, List[int]]:
    """
    0-1 Knapsack Problem Solver
    :param items: Item List
    :param weight: Limit Weight
    :return: Max Value and Selection List
    """
    # Append None to the head of item list
    inner_items: List[Item] = [Item(0, 0)]
    inner_items.extend(items)
    n: int = len(inner_items)

    # Initialize Tables
    value_table: List[List[int]] = [[0 for j in range(weight + 1)] for i in range(n)]
    selection_table: List[List[int]] = [[DIAGONAL if i == 0 else TOP for j in range(weight + 1)] for i in range(n)]

    # Solve
    for i in range(1, n):
        inner_item: Item = inner_items[i]
        for j in range(1, weight + 1):
            value_table[i][j] = value_table[i - 1][j]
            selection_table[i][j] = TOP
            if inner_item.weight > j:
                continue
            if inner_item.value + value_table[i - 1][j - inner_item.weight] > value_table[i][j]:
                value_table[i][j] = inner_item.value + value_table[i - 1][j - inner_item.weight]
                selection_table[i][j] = DIAGONAL

    # Return Results
    selection: Deque[int] = deque()
    w: int = weight
    for i in range(n - 1, 0, -1):
        inner_item = inner_items[i]
        if selection_table[i][w] == DIAGONAL:
            selection.appendleft(i)
            w -= inner_item.weight

    return value_table[n - 1][weight], list(selection)

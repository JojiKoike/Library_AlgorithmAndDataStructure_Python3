"""
Dynamic Programming Method Module
"""
from typing import List, Tuple, Deque
from collections import deque
import bisect
from .common import INFINITY, DIAGONAL, TOP
from .structs import Item, Rectangle


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


def lis(a: List[int]) -> int:
    """
    Longest Increasing Subsequence Length Calculator
    :param a:
    :return: Length
    """
    n: int = len(a)
    l: List[int] = [0 for i in range(n)]
    l[0] = a[0]
    length: int = 1
    for i in range(1, n):
        if l[length - 1] < a[i]:
            l[length] = a[i]
            length += 1
        else:
            l[bisect.bisect_left(l, a[i], 0, length - 1)] = a[i]

    return length


def get_largest_square(g: List[List[int]]) -> int:
    h: int = len(g)
    w: int = len(g[0])
    dp: List[List[int]] = [[0 for j in range(w)] for i in range(h)]
    max_width: int = 0

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                dp[i][j] = (g[i][j] + 1) % 2
                max_width |= dp[i][j]

    for i in range(1, h):
        for j in range(1, w):
            if g[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                max_width = max(max_width, dp[i][j])

    return max_width * max_width


def get_largest_rectangle(g: List[List[int]]) -> int:
    h: int = len(g)
    w: int = len(g[0])
    t: List[List[int]] = [[0 for j in range(w)] for i in range(h)]

    for j in range(w):
        for i in range(h):
            if g[i][j] == 1:
                t[i][j] = 0
            else:
                t[i][j] = t[i - 1][j] + 1 if i > 0 else 1

    max_reactangle: int = 0
    for i in range(h):
        max_reactangle = max(max_reactangle, _get_largest_rectangle(t[i]))

    return max_reactangle


def _get_largest_rectangle(t: List[int]) -> int:
    stack: List[Rectangle] = []
    max_v: int = 0
    for i in range(len(t)):
        rect: Rectangle = Rectangle(t[i], i)
        if len(stack) == 0:
            stack.append(rect)
        else:
            if stack[len(stack) - 1].height < rect.height:
                stack.append(rect)
            elif stack[len(stack) - 1].height > rect.height:
                target: int = i
                while len(stack) > 0 and stack[len(stack) - 1].height >= rect.height:
                    pre_rect: Rectangle = stack.pop()
                    area: int = pre_rect.height * (i - pre_rect.pos)
                    max_v = max(max_v, area)
                    target = pre_rect.pos
                rect.pos = target
                stack.append(rect)
    return max_v

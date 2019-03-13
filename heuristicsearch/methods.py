"""
Heuristic Search Methods Module
"""
from typing import List, Optional
from .common import N_EIGHT, FREE, NOT_FREE
from .structs import Queen

x: List[List[bool]] = []
row: List[int] = []
col: List[int] = []
dpos: List[int] = []
dneg: List[int] = []
res: List[List[str]] = []


def eight_queen_solver(queens: List[Queen]) -> List[List[str]]:
    global res
    # Initialize
    __eight_queen_initialize(queens)

    # Solve
    __recursive(0)

    return res


def __eight_queen_initialize(queens: List[Queen]) -> None:
    global x, row, col, dpos, dneg
    x = [[False for i in range(N_EIGHT)] for i in range(N_EIGHT)]
    for queen in queens:
        x[queen.row][queen.col] = True
    row = [FREE for j in range(N_EIGHT)]
    col = [FREE for k in range(N_EIGHT)]
    dpos = [FREE for l in range(2 * N_EIGHT - 1)]
    dneg = [FREE for m in range(2 * N_EIGHT - 1)]


def __recursive(i: int) -> None:
    global row, col, dpos, dneg
    if i == N_EIGHT:
        __print_board()
        return
    for j in range(N_EIGHT):
        if col[j] == NOT_FREE or \
                dpos[i + j] == NOT_FREE or \
                dneg[i - j + N_EIGHT - 1] == NOT_FREE:
            continue
        # Allocate Queen at (i, j)
        row[i] = j
        col[j] = dpos[i + j] = dneg[i - j + N_EIGHT - 1] = NOT_FREE
        # Tri Next Row
        __recursive(i + 1)
        # Back Tracking (Deallocate Queen at (i, j))
        row[i] = col[j] = dpos[i + j] = dneg[i - j + N_EIGHT - 1] = FREE


def __print_board() -> None:
    global row, x, res
    for i in range(N_EIGHT):
        for j in range(N_EIGHT):
            if x[i][j]:
                if row[i] != j:
                    return
    res = [['' for j in range(N_EIGHT)] for i in range(N_EIGHT)]
    for i in range(N_EIGHT):
        for j in range(N_EIGHT):
            res[i][j] = 'Q' if row[i] == j else '.'

"""
Heuristic Search Methods Module
"""
from typing import List, Deque, Dict
from collections import deque
import copy
from .common import N_EIGHT, FREE, \
    NOT_FREE, N_EIGHT_PUZZLE, N2_EIGHT_PUZZLE, \
    dx, dy, dir, N_16_PUZZLE, N2_16_PUZZLE, LIMIT
from .structs import Queen, Puzzle, Puzzle2

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


def eight_puzzle_solver(data: List[int]) -> int:
    space: int = data.index(0)
    data[space] = N2_EIGHT_PUZZLE
    puzzle: Puzzle = Puzzle(data, space, '')
    res: str = _eight_puzzle_bfs(puzzle)
    return len(res)


def _eight_puzzle_bfs(puzzle: Puzzle) -> str:
    q: Deque[Puzzle] = deque()
    p_map: Dict[Puzzle, bool] = {}
    puzzle.path = ""
    q.append(puzzle)
    p_map[puzzle] = True

    while len(q) > 0:
        u: Puzzle = q.popleft()
        if __is_target(u):
            return u.path
        sx: int = int(u.space / N_EIGHT_PUZZLE)
        sy: int = u.space % N_EIGHT_PUZZLE
        for r in range(4):
            tx: int = sx + dx[r]
            ty: int = sy + dy[r]
            if tx < 0 or ty < 0 or \
                    tx >= N_EIGHT_PUZZLE or ty >= N_EIGHT_PUZZLE:
                continue
            v: Puzzle = copy.deepcopy(u)
            v.f[u.space], v.f[tx * N_EIGHT_PUZZLE + ty] \
                = v.f[tx * N_EIGHT_PUZZLE + ty], v.f[u.space]
            v.space = tx * N_EIGHT_PUZZLE + ty
            if v not in p_map:
                p_map[v] = True
                v.path += dir[r]
                q.append(v)
    return "unsolvable"


def __is_target(puzzle: Puzzle) -> bool:
    for i in range(N2_EIGHT_PUZZLE):
        if puzzle.f[i] != i + 1:
            return False
    return True


mdt: List[List[int]] = [[0 for j in range(N2_16_PUZZLE)] for i in range(N2_16_PUZZLE)]
limit: int = 0
state: Puzzle2
path: List[int] = [0 for i in range(LIMIT)]


def sixteen_puzzle_solver_ida_star(data: List[int]) -> int:
    global mdt
    # Build Manhattan Distance Table
    for i in range(N2_16_PUZZLE):
        for j in range(N2_16_PUZZLE):
            mdt[i][j] = abs(int(i / N_16_PUZZLE) - int(j / N_16_PUZZLE)) \
                        + abs(i % N_16_PUZZLE - j % N_16_PUZZLE)
    space: int = data.index(0)
    data[space] = N2_16_PUZZLE
    puzzle: Puzzle2 = Puzzle2(data, space, 0)
    ans: str = __iterative_deeping(puzzle)
    return len(ans)


def __iterative_deeping(puzzle: Puzzle2) -> str:
    puzzle.MD = __get_all_md(puzzle)
    global limit, state, path
    limit = puzzle.MD
    while limit <= LIMIT:
        state = copy.deepcopy(puzzle)
        if __dfs(0, -100):
            ans: str = ""
            for i in range(limit):
                ans += dir[path[i]]
            return ans
        limit += 1
    return "unsolvable"


def __get_all_md(puzzle: Puzzle2) -> int:
    global mdt
    sum: int = 0
    for i in range(N2_16_PUZZLE):
        if puzzle.f[i] == N2_16_PUZZLE:
            continue
        sum += mdt[i][puzzle.f[i] - 1]
    return sum


def __dfs(depth: int, prev: int) -> bool:
    global state, limit
    if state.MD == 0:
        return True
    if depth + state.MD > limit:
        return False
    sx: int = int(state.space / N_16_PUZZLE)
    sy: int = state.space % N_16_PUZZLE
    tmp: Puzzle2
    for r in range(4):
        tx: int = sx + dx[r]
        ty: int = sy + dy[r]
        if tx < 0 or ty < 0 or tx >= N_16_PUZZLE or ty >= N_16_PUZZLE:
            continue
        if max(prev, r) - min(prev, r) == 2:
            continue
        tmp = copy.deepcopy(state)
        state.MD -= mdt[tx * N_16_PUZZLE + ty][state.f[tx * N_16_PUZZLE + ty] - 1]
        state.MD += mdt[sx * N_16_PUZZLE + sy][state.f[tx * N_16_PUZZLE + ty] - 1]
        state.f[tx * N_16_PUZZLE + ty], state.f[sx * N_16_PUZZLE + sy] = \
            state.f[sx * N_16_PUZZLE + sy], state.f[tx * N_16_PUZZLE + ty]
        state.space = tx * N_16_PUZZLE + ty
        if __dfs(depth + 1, r):
            path[depth] = r
            return True
        state = tmp
    return False


def __is_solved():
    for i in range(N2_16_PUZZLE):
        if state.f[i] != i + 1:
            return False
    return True

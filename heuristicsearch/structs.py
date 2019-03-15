"""
Heuristic Search Structs Module
"""
from dataclasses import dataclass
from typing import List
from .common import N2_EIGHT_PUZZLE, N2_16_PUZZLE


@dataclass
class Queen:
    row: int
    col: int


class Puzzle:

    def __init__(self, f: List[int], space: int, path: str):
        self.f = f
        self.space = space
        self.path = path

    def __lt__(self, other):
        for i in range(N2_EIGHT_PUZZLE):
            if self.f[i] == other.f[i]:
                continue
            return self.f[i] > other.f[i]
        return False


@dataclass
class Puzzle2:
    f: List[int]
    space: int
    MD: int


class Puzzle3:
    def __init__(self, f: List[int], space: int, md: int, cost: int):
        self.f = f
        self.space = space
        self.MD = md
        self.cost = cost

    def __lt__(self, other):
        for i in range(N2_16_PUZZLE):
            if self.f[i] == other.f[i]:
                continue
            return self.f[i] < other.f[i]
        return False


class State:
    def __init__(self, puzzle: Puzzle3, estimated: int):
        self.puzzle = puzzle
        self.estimated = estimated

    def __lt__(self, other):
        return self.estimated < other.estimated

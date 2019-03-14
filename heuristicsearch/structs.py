"""
Heuristic Search Structs Module
"""
from dataclasses import dataclass
from typing import List
from .common import N2_EIGHT_PUZZLE


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



"""
Heuristic Search Structs Module
"""
from dataclasses import dataclass


@dataclass
class Queen:
    row: int
    col: int

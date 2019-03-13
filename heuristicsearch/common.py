"""
Heuristic Search Common Module
"""
from typing import List

N_EIGHT: int = 8
FREE: int = -1
NOT_FREE: int = 1

N_EIGHT_PUZZLE: int = 3
N2_EIGHT_PUZZLE: int = 9

dx: List[int] = [-1, 0, 1, 0]
dy: List[int] = [0, -1, 0, 1]
dir: List[str] = ['u', 'l', 'd', 'r']

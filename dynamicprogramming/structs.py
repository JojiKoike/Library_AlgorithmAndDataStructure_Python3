"""
Dynamic Programming Structs Module
"""
from dataclasses import dataclass


@dataclass
class Item:
    """
    Item Data Structure
    """
    weight: int
    value: int

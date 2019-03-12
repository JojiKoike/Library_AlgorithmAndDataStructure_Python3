"""
Dynamic Programming Structs Module
"""
from dataclasses import dataclass


@dataclass
class Item:
    """
    Item Data Structure
    """
    value: int
    weight: int


@dataclass
class Rectangle:
    """
    Rectangle Data Structure
    """
    height: int
    pos: int

"""
Data Structure Definitions Module
"""
from dataclasses import dataclass


@dataclass
class Point:
    """
    Point in x-y plane
    """
    x: float
    y: float

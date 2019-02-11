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


@dataclass
class Segment:
    """
    Segment in x-y plane
    """
    p1: Point
    p2: Point


@dataclass
class Circle:
    """
    Circle in x-y plane
    """
    c: Point
    r: float

"""
Data Structure Definitions Module
"""
from dataclasses import dataclass
import math
from .common import EPS


@dataclass
class Point:
    """
    Point in x-y plane
    """
    x: float
    y: float

    def abs(self) -> float:
        """
        Calculate Length
        :return: Distance From Origin(0, 0)
        """
        return math.sqrt(math.pow(self.x, 2.0) + math.pow(self.y, 2.0))

    def norm(self) -> float:
        """
        Calculate Norm
        :return: Norm
        """
        return math.pow(self.x, 2.0) + math.pow(self.y, 2.0)

    def __lt__(self, other) -> bool:
        """
        Less Than Rule
        :param other: Other Point
        :return: Less Than Compare Result
        """
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __eq__(self, other) -> bool:
        """
        Equality Definition
        :param other: Other Point
        :return: Equality Calculation Result
        """
        return math.fabs(self.x - other.x) < EPS and math.fabs(self.y - other.y) < EPS



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

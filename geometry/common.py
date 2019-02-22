"""
Common module for geometry
"""
from enum import Enum

# EPS is acceptable error
EPS: float = 1e-10


def equals(x_0: float, x_1: float) -> bool:
    """
    Equality Calculation considering float precision
    :param x_0: One Coordinate Value
    :param x_1: Other Coordinate Value
    :return: Equality Calculation Result
    """
    return abs(x_0 - x_1) < EPS


class PointRelativePosition(Enum):
    """
    Point relative position ENUM
    """
    COUNTER_CLOCK_WISE: int = 1
    CLOCK_WISE: int = -1
    ON_LINE_FRONT: int = 2
    ON_LINE_BACK: int = -2
    ON_SEGMENT: int = 0


class PointContainsInPolygon(Enum):
    """
    Point Contained in Polygon Status
    """
    IN: int = 2
    ON_EDGE: int = 1
    OUT: int = 0


class EndPointType(Enum):
    """
    Segment Endpoint Type
    """
    BOTTOM: int = 0
    LEFT: int = 1
    RIGHT: int = 2
    TOP: int = 3

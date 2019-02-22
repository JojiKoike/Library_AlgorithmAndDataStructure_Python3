"""
Data Structure Definitions Module
"""
from dataclasses import dataclass
from typing import List, Optional
import math
import sys
import traceback
from geometry.common import EPS, EndPointType


class Point(object):
    """
    Point in x-y plane
    """
    def __init__(self, x_0: float, y_0: float):
        self.x = x_0
        self.y = y_0

    def __add__(self, other):
        """
        Add Calculation Definition
        :param other: Add Operand Point
        :return: Point
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subs. Calculation Definition
        :param other: Subs. Operand Point
        :return: Point
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, a_0: float):
        """
        Enlargement
        :param a_0 : Enlargement Factor
        :return:
        """
        return Point(self.x * a_0, self.y * a_0)

    def __truediv__(self, a_0: float):
        """
        Reduction
        :param a_0: Reduction Factor
        :return: Point
        """
        res: Optional[Point] = None
        try:
            res = Point(self.x / a_0, self.y / a_0)
        except ZeroDivisionError as e_0:
            print("ERROR :  Zero Division!!!")
            print(e_0)
            sys.stderr.write(traceback.format_exc())
        return res

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
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS


class Vector(Point):
    """
    Vector in x-y plane
    """
    def dot(self, other) -> float:
        """
        Calculate Vector dot product
        :param other: Vector
        :return: Dot Product Result
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> float:
        """
        Calculate Vector cross product
        :param other: Vector
        :return: Cross Product Result
        """
        return self.x * other.y - other.x * self.y


class Segment(object):
    """
    Segment in x-y plane
    """
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


class Line(Segment):
    """
    Line in x-y plane
    """


@dataclass
class Polygon:
    """
    Polygon in x-y plane
    """
    p_i: List[Point]


@dataclass
class Circle:
    """
    Circle in x-y plane
    """
    c: Point
    r: float


class EndPoint(object):
    """
    Segment Endpoint Data Structure
    """
    def __init__(self, p: Point, seg_id: int, end_point_type: EndPointType):
        self.p = p
        self.seg = seg_id
        self.st = end_point_type

    def __lt__(self, other):
        if self.p.y == other.p.y:
            return self.st < other.st
        else:
            return self.p.y < other.p.y

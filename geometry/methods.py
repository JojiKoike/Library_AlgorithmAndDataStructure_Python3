"""
Geometry Methods Module
"""
from typing import Optional
from geometry.structs import Point, Vector, Segment, Line
from geometry.common import equals, PointRelativePosition, EPS


def is_orthogonal(*args) -> Optional[bool]:
    """
    Orthogonal Judgement
    :param args: Two Vectors or Four Points or Two Segments
    :return: Optional[bool]
    """
    len_args: int = len(args)
    if len_args == 2:
        if isinstance(args[0], Vector):
            v_1: Vector = args[0]
            v_2: Vector = args[1]
        elif isinstance(args[0], Segment):
            s_1: Segment = args[0]
            s_2: Segment = args[1]
            v_1 = Vector((s_1.p1 - s_1.p2).x, (s_1.p1 - s_1.p2).y)
            v_2 = Vector((s_2.p1 - s_2.p2).x, (s_2.p1 - s_2.p2).y)
        else:
            raise TypeError("Error: TypeError")
    elif len_args == 4:
        if isinstance(args[0], Point):
            p_1: Point = args[0]
            p_2: Point = args[1]
            p_3: Point = args[2]
            p_4: Point = args[3]
            v_1 = Vector((p_1 - p_2).x, (p_1 - p_2).y)
            v_2 = Vector((p_3 - p_4).x, (p_3 - p_4).y)
        else:
            raise TypeError("Error: TypeError")
    else:
        raise TypeError("Error: Argument Error")
    return equals(v_1.dot(v_2), 0.0)


def is_parallel(*args) -> Optional[bool]:
    """
    Parallel Judgement
    :param args: Two Vectors or Four Points or Two Segments
    :return: Optional[bool]
    """
    len_args: int = len(args)
    if len_args == 2:
        if isinstance(args[0], Vector):
            v_1: Vector = args[0]
            v_2: Vector = args[1]
        elif isinstance(args[0], Segment):
            s_1: Segment = args[0]
            s_2: Segment = args[1]
            v_1 = Vector((s_1.p1 - s_1.p2).x, (s_1.p1 - s_1.p2).y)
            v_2 = Vector((s_2.p1 - s_2.p2).x, (s_2.p1 - s_2.p2).y)
        else:
            raise TypeError("Error: Argument Type Error")
    elif len_args == 4:
        if isinstance(args[0], Point):
            p_1: Point = args[0]
            p_2: Point = args[1]
            p_3: Point = args[2]
            p_4: Point = args[3]
            v_1 = Vector((p_1 - p_2).x, (p_1 - p_2).y)
            v_2 = Vector((p_3 - p_4).x, (p_3 - p_4).y)
        else:
            raise TypeError("Error: Argument Type Error")
    else:
        raise TypeError("Error: Argument Error")
    return equals(v_1.cross(v_2), 0.0)


def project(s: Segment, p: Point) -> Point:
    """
    Calculate Point Projection on the Segment
    :param s: Projection base segment
    :param p: Projection Point
    :return: Projected Coordinate Value
    """
    hypo: Vector = Vector(p.x - s.p1.x, p.y - s.p1.y)
    base: Vector = Vector(s.p2.x - s.p1.x, s.p2.y - s.p1.y)
    r: float = hypo.dot(base) / base.norm()
    return s.p1 + base * r


def reflect(s: Segment, p: Point) -> Point:
    """
    Calculate Reflected Point Coordinate Value
    :param s: Segment for Reflection Axis
    :param p: Reflect Target Point
    :return: Reflected Point Coordinate Value
    """
    return p + (project(s, p) - p) * 2.0


def get_distance(a: Point, b: Point) -> float:
    """
    Calculate Distance between two points
    :param a: One Point
    :param b: The Other Point
    :return: Distance Between provided two points
    """
    return (a - b).abs()


def get_distance_lp(l: Line, p: Point) -> float:
    """
    Calculate Distance between point and line
    :param l: Line
    :param p: Point
    :return: Distance between provided point and line
    """
    v_1: Vector = Vector(p.x - l.p1.x, p.y - l.p1.y)
    v_2: Vector = Vector(l.p2.x - l.p1.x, l.p2.y - l.p1.y)
    return abs(v_2.cross(v_1)) / v_2.abs()


def get_distance_sp(s: Segment, p: Point) -> float:
    """
    Calculate Distance between point and segment
    :param s: Segment
    :param p: Point
    :return: Distance between provided point and segment
    """
    v_1: Vector = Vector((p - s.p1).x, (p - s.p2).y)
    v_2: Vector = Vector((p - s.p2).x, (p - s.p2).y)
    v_base: Vector = Vector((s.p2 - s.p1).x, (s.p2 - s.p1).y)
    if v_1.dot(v_base) < 0:
        return (p - s.p1).abs()
    if v_2.dot(v_base) > 0:
        return (p - s.p2).abs()
    return get_distance_lp(Line(s.p1, s.p2), p)


def get_point_relative_position(p_0: Point, p_1: Point, p_2: Point) \
        -> PointRelativePosition:
    """
    Calculate Point Relative Position
    :param p_0: Origin Point
    :param p_1: Point
    :param p_2: Point
    :return: PointRelativePosition
    """
    v_1: Vector = Vector((p_1 - p_0).x, (p_1 - p_0).y)
    v_2: Vector = Vector((p_2 - p_0).x, (p_2 - p_0).y)
    if v_1.cross(v_2) > EPS:
        return PointRelativePosition.COUNTER_CLOCK_WISE
    if v_1.cross(v_2) < -EPS:
        return PointRelativePosition.CLOCK_WISE
    if v_1.dot(v_2) < -EPS:
        return PointRelativePosition.ON_LINE_BACK
    if v_1.norm() < v_2.norm():
        return PointRelativePosition.ON_LINE_FRONT
    return PointRelativePosition.ON_SEGMENT

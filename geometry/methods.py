"""
Geometry Methods Module
"""
from typing import Optional, List
import math
from geometry.structs import Point, Vector, Segment, Line, Circle, Polygon
from geometry.common import equals, PointRelativePosition, EPS, PointContainsInPolygon


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


def get_distance_ss(s_1: Segment, s_2: Segment) -> float:
    """
    Calculate distance between two segments
    :param s_1: One Segment
    :param s_2: The Other Segment
    :return: Distance Between provided two segments
    """
    if intersect(s_1, s_2):
        return 0
    return min(min(get_distance_sp(s_2, s_1.p1), get_distance_sp(s_2, s_1.p2)),
               min(get_distance_sp(s_1, s_2.p1), get_distance_sp(s_1, s_2.p2)))


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


def intersect(s_1: Segment, s_2: Segment) -> bool:
    """
    Calc. Segment Intersection
    :param s_1: One Segment
    :param s_2: The other Segment
    :return: Segment Intersect each other (bool)
    """
    v_1: Vector = Vector((s_1.p2 - s_1.p1).x, (s_1.p2 - s_1.p2).y)
    v_11: Vector = Vector((s_2.p1 - s_1.p1).x, (s_2.p1 - s_1.p1).y)
    v_12: Vector = Vector((s_2.p2 - s_1.p1).x, (s_2.p2 - s_1.p1).y)
    v_2: Vector = Vector((s_2.p2 - s_2.p1).x, (s_2.p2 - s_2.p1).y)
    v_21: Vector = Vector((s_1.p1 - s_2.p1).x, (s_1.p1 - s_2.p1).y)
    v_22: Vector = Vector((s_1.p2 - s_2.p1).x, (s_1.p2 - s_2.p1).y)
    return (v_1.cross(v_11) * v_1.cross(v_12) <= 0) and (v_2.cross(v_21) * v_2.cross(v_22) <= 0)


def get_cross_point(s_1: Segment, s_2: Segment) -> Optional[Point]:
    """
    Calculate Segment Cross Point
    :param s_1: One Segment
    :param s_2: The Other Segment
    :return: Cross Point Coordinate Value if intersects
    """
    if intersect(s_1, s_2):
        v_base: Vector = Vector((s_2.p2 - s_2.p1).x, (s_2.p2 - s_2.p1).y)
        v_hypo1: Vector = Vector((s_1.p1 - s_2.p1).x, (s_1.p1 - s_2.p1).y)
        v_hypo2: Vector = Vector((s_1.p2 - s_2.p1).x, (s_1.p2 - s_2.p1).y)
        v: Vector = Vector((s_1.p2 - s_1.p1).x, (s_1.p2 - s_1.p1).y)
        d1: float = abs(v_base.cross(v_hypo1))
        d2: float = abs(v_base.cross(v_hypo2))
        p: Vector = Vector(s_1.p1.x, s_1.p1.y) + v * (d1 / (d1 + d2))
        return Point(p.x, p.y)
    return None


def get_cross_points_circle_and_line(circle: Circle, line: Line) -> Optional[List[Point]]:
    """
    Calculate Line and Circle Cross Point Coordinate Values
    :param circle: Circle
    :param line: Line
    :return: Cross Point or Contact Point
    """
    res: List[Point] = []
    d: float = get_distance_lp(line, circle.c)
    if circle.r - d > EPS:
        p: Point = project(line, circle.c)
        e: float = math.sqrt(math.pow(circle.r, 2.0) - math.pow(d, 2.0))
        v_base: Vector = Vector((line.p2 - line.p1).x, (line.p2 - line.p1).y)
        x_1: Vector = Vector(p.x, p.y) + v_base * e / v_base.abs()
        x_2: Vector = Vector(p.x, p.y) - v_base * e / v_base.abs()
        res.append(Point(x_1.x, x_1.y))
        res.append(Point(x_2.x, x_2.y))
        return res
    elif equals(circle.r, d):
        res.append(project(line, circle.c))
        return res
    return None


def get_common_points_circle_and_circle(c_1: Circle, c_2: Circle) -> Optional[List[Point]]:
    """
    Calculate Two Circle Common Points
    :param c_1: One Circle
    :param c_2: The Other Circle
    :return: None: Not Intersect or Duplicate, List[Point] : Contacts or Intersects
    """
    d: float = (c_1.c - c_2.c).abs()  # Distance Between Circle Centers
    res: List[Point] = []
    if c_1.c == c_2.c and equals(c_1.r, c_2.r) \
            or c_1.r + c_2.r < d or abs(c_1.r - c_2.r) > d:
        # Completely Duplicates or Not Contacts and Intersects
        return None
    if equals(c_1.r + c_2.r, d) or equals(abs(c_1.r - c_2.r), d):
        # Contacts Each Other
        c_larger: Circle = c_1 if c_1.r >= c_2.r else c_2
        c_smaller: Circle = c_1 if c_1.r < c_2.r else c_2
        v_c1_c2: Vector = Vector((c_smaller.c - c_larger.c).x, (c_smaller.c - c_larger.c).y)
        x_c: Vector = Vector(c_larger.c.x, c_larger.c.y) + v_c1_c2 * (c_larger.r / d)
        res.append(Point(x_c.x, x_c.y))
    if abs(c_1.r - c_2.r) < d < c_1.r + c_2.r:
        # Intersects
        t: float = (math.pi / 2.0 if c_1.c.y < c_2.c.y else -math.pi / 2.0)\
            if c_1.c.x == c_2.c.x \
            else math.atan(abs((c_2.c - c_1.c).y / (c_2.c - c_1.c).x))
        alpha: float = \
            math.acos((c_1.r * c_1.r + d * d - c_2.r * c_2.r) / (2 * c_1.r * d))
        v_1: Vector = Vector(c_1.c.x, c_1.c.y) + \
            Vector(c_1.r * math.cos(t + alpha), c_1.r * math.sin(t + alpha))
        v_2: Vector = Vector(c_1.c.x, c_1.c.y) + \
            Vector(c_1.r * math.cos(t - alpha), c_1.r * math.sin(t - alpha))
        res.append(Point(v_1.x, v_1.y))
        res.append(Point(v_2.x, v_2.y))
    return res


def point_contained_in_polygon(poly: Polygon, p: Point) -> PointContainsInPolygon:
    """
    Calculate Is Point Contained in Polygon
    :param poly: Polygon
    :param p: Point
    :return: PointContainsInPolygon
    """
    n: int = len(poly.p_i)  # Number of Nodes of Polygon
    count_intersect: int = 0
    for i in range(n):
        a: Point = poly.p_i[i] - p
        b: Point = poly.p_i[(i + 1) % n] - p
        v_1: Vector = Vector(a.x, a.y)
        v_2: Vector = Vector(b.x, b.y)
        if v_1.dot(v_2) < 0 and equals(v_1.cross(v_2), 0):
            return PointContainsInPolygon.ON_EDGE
        if a.y > b.y:
            a, b = b, a
            v_1 = Vector(a.x, a.y)
            v_2 = Vector(b.x, b.y)
        if a.y < EPS < b.y and v_1.cross(v_2) > EPS:
            count_intersect += 1
    return PointContainsInPolygon.IN \
        if count_intersect % 2 == 1 else PointContainsInPolygon.OUT


def get_convex_hull(g: Polygon) -> Polygon:
    """
    Solve Convex Hull with Andrew Algorithm
    :param g: Polygon
    :return: Convex Hull Polygon
    """
    if len(g.p_i) < 3:
        return g
    g.p_i.sort()
    poly_u: Polygon = Polygon([])
    poly_l: Polygon = Polygon([])
    poly_u.p_i.append(g.p_i[0])
    poly_u.p_i.append(g.p_i[1])
    poly_l.p_i.append(g.p_i[len(g.p_i) - 1])
    poly_l.p_i.append(g.p_i[len(g.p_i) - 2])

    # Build Convex Hull Upper Part
    for i in range(2, len(g.p_i)):
        for j in range(len(poly_u.p_i), 1, -1):
            if get_point_relative_position(poly_u.p_i[j - 2],
                                           poly_u.p_i[j - 1],
                                           g.p_i[i]) == PointRelativePosition.COUNTER_CLOCK_WISE:
                poly_u.p_i.pop()
        poly_u.p_i.append(g.p_i[i])

    # Build Convex Hull Lower Part
    for i in range(len(g.p_i) - 3, -1, -1):
        for j in range(len(poly_l.p_i), 1, -1):
            if get_point_relative_position(poly_l.p_i[j - 2],
                                           poly_l.p_i[j - 1],
                                           g.p_i[i]) == PointRelativePosition.COUNTER_CLOCK_WISE:
                poly_l.p_i.pop()
        poly_l.p_i.append(g.p_i[i])

    # Build Convex Hull Nodes List
    poly_l.p_i.sort()
    for i in range(len(poly_u.p_i) - 2, 0, -1):
        poly_l.p_i.append(poly_u.p_i[i])

    return poly_l

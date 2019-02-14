from typing import Optional
from geometry.structs import Point, Vector, Segment
from geometry.common import equals


def is_orthogonal(*args) -> Optional[bool]:
    len_args: int = len(args)
    v_1: Optional[Vector] = None
    v_2: Optional[Vector] = None
    if len_args == 2:
        if isinstance(args[0], Vector):
            v_1 = args[0]
            v_2 = args[1]
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
        raise TypeError("Error: Argument Error")
    return equals(v_1.dot(v_2), 0.0)

EPSILON = 1e-9


def is_close(a: float, b: float, eps: float = EPSILON) -> bool:
    return abs(a - b) < eps


def bounding_box(points):
    from .point import Point
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    return Point(min(xs), min(ys)), Point(max(xs), max(ys))

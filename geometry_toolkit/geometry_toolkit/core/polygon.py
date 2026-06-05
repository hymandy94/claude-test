from .point import Point
from .utils import is_close


def point_in_polygon(p: Point, vertices: list[Point]) -> bool:
    n = len(vertices)
    inside = False
    j = n - 1
    for i in range(n):
        yi, yj = vertices[i].y, vertices[j].y
        xi, xj = vertices[i].x, vertices[j].x
        if ((yj > p.y) != (yi > p.y)) and (p.x < (xj - xi) * (p.y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


def polygon_area(vertices: list[Point]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i].x * vertices[j].y
        area -= vertices[j].x * vertices[i].y
    return abs(area) / 2.0


def convex_hull(points: list[Point]) -> list[Point]:
    pts = sorted(points, key=lambda p: (p.x, p.y))
    if len(pts) <= 1:
        return list(pts)

    def cross(o, a, b):
        return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

    lower: list[Point] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: list[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

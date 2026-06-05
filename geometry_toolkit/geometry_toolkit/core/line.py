from dataclasses import dataclass
from .point import Point
from .utils import is_close


@dataclass(frozen=True)
class LineSegment:
    start: Point
    end: Point

    @property
    def dx(self) -> float:
        return self.end.x - self.start.x

    @property
    def dy(self) -> float:
        return self.end.y - self.start.y

    @property
    def length(self) -> float:
        return self.start.distance_to(self.end)


def intersect_lines(l1: LineSegment, l2: LineSegment) -> Point | None:
    d1x, d1y = l1.dx, l1.dy
    d2x, d2y = l2.dx, l2.dy
    cross = d1x * d2y - d1y * d2x
    if is_close(cross, 0.0):
        return None
    dx = l2.start.x - l1.start.x
    dy = l2.start.y - l1.start.y
    t = (dx * d2y - dy * d2x) / cross
    return Point(l1.start.x + t * d1x, l1.start.y + t * d1y)


def point_to_line_distance(p: Point, line: LineSegment) -> float:
    length = line.length
    if is_close(length, 0.0):
        return p.distance_to(line.start)
    return abs(line.dx * (line.start.y - p.y) - line.dy * (line.start.x - p.x)) / length


def line_equation(line: LineSegment) -> tuple[float, float, float]:
    a, b, c = line.dy, -line.dx, line.dx * line.start.y - line.dy * line.start.x
    norm = (a * a + b * b) ** 0.5
    return a / norm, b / norm, c / norm

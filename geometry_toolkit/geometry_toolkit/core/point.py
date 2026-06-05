"""二维点数据类与几何变换函数。

提供不可变的 ``Point`` 数据类（支持欧氏距离计算），
以及中点、平移、旋转、缩放等独立变换函数。
所有变换函数均返回新的 ``Point`` 对象，不会修改输入。

角度参数单位为弧度。
"""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """不可变的二维点，包含 ``x`` 和 ``y`` 坐标。

    由于数据类是冻结的，实例可哈希，可作为字典键或放入集合中。
    """

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        """计算两点之间的欧氏距离。

        内部使用 ``math.hypot`` 保证数值稳定性。
        """
        return math.hypot(other.x - self.x, other.y - self.y)


def midpoint(a: Point, b: Point) -> Point:
    """返回 *a* 和 *b* 的中点。"""
    return Point((a.x + b.x) / 2, (a.y + b.y) / 2)


def translate_point(p: Point, dx: float, dy: float) -> Point:
    """Return a new point translated by (*dx*, *dy*).

    The original point *p* is not modified.
    """
    return Point(p.x + dx, p.y + dy)


def rotate_point(p: Point, angle: float, center: Point | None = None) -> Point:
    """Return a new point rotated by *angle* radians around *center*.

    If *center* is ``None``, rotation is around the origin ``(0, 0)``.
    Positive angles represent counter-clockwise rotation.
    """
    cx, cy = (center.x, center.y) if center else (0.0, 0.0)
    dx, dy = p.x - cx, p.y - cy
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return Point(cx + dx * cos_a - dy * sin_a, cy + dx * sin_a + dy * cos_a)


def scale_point(p: Point, factor: float, center: Point | None = None) -> Point:
    """Return a new point scaled by *factor* relative to *center*.

    If *center* is ``None``, scaling is relative to the origin ``(0, 0)``.
    A factor greater than 1 enlarges the distance from the center;
    a factor between 0 and 1 shrinks it.
    """
    cx, cy = (center.x, center.y) if center else (0.0, 0.0)
    return Point(cx + (p.x - cx) * factor, cy + (p.y - cy) * factor)

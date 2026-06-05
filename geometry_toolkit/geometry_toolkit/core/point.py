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
    """返回沿 (*dx*, *dy*) 平移后的新点。

    原始点 *p* 不会被修改。
    """
    return Point(p.x + dx, p.y + dy)


def rotate_point(p: Point, angle: float, center: Point | None = None) -> Point:
    """返回绕 *center* 旋转 *angle* 弧度后的新点。

    若 *center* 为 ``None``，则绕原点 ``(0, 0)`` 旋转。
    正角度表示逆时针旋转。
    """
    cx, cy = (center.x, center.y) if center else (0.0, 0.0)
    dx, dy = p.x - cx, p.y - cy
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    return Point(cx + dx * cos_a - dy * sin_a, cy + dx * sin_a + dy * cos_a)


def scale_point(p: Point, factor: float, center: Point | None = None) -> Point:
    """返回相对于 *center* 缩放 *factor* 倍后的新点。

    若 *center* 为 ``None``，则相对于原点 ``(0, 0)`` 缩放。
    缩放因子大于 1 时远离中心，0 到 1 之间时靠近中心。
    """
    cx, cy = (center.x, center.y) if center else (0.0, 0.0)
    return Point(cx + (p.x - cx) * factor, cy + (p.y - cy) * factor)

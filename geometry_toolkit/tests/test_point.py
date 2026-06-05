"""
Test for points
"""
import math
import pytest
from geometry_toolkit.core.point import Point, midpoint, translate_point, rotate_point


class TestDistanceTo:
    def test_same_point(self):
        p = Point(3, 4)
        assert p.distance_to(p) == pytest.approx(0.0)

    def test_same_x(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        assert p1.distance_to(p2) == pytest.approx(5.0)

    def test_same_y(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        assert p1.distance_to(p2) == pytest.approx(3.0)

    def test_diagonal(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        assert p1.distance_to(p2) == pytest.approx(5.0)

    def test_negative_coords(self):
        p1 = Point(-1, -1)
        p2 = Point(1, 1)
        assert p1.distance_to(p2) == pytest.approx(math.sqrt(8))


class TestMidpoint:
    def test_basic(self):
        assert midpoint(Point(0, 0), Point(2, 2)) == Point(1, 1)

    def test_negative(self):
        assert midpoint(Point(-2, -4), Point(2, 0)) == Point(0, -2)

    def test_same_point(self):
        p = Point(5, 7)
        assert midpoint(p, p) == p


class TestTranslatePoint:
    def test_positive(self):
        result = translate_point(Point(1, 1), dx=3, dy=4)
        assert result == Point(4, 5)

    def test_negative(self):
        result = translate_point(Point(5, 5), dx=-2, dy=-3)
        assert result == Point(3, 2)

    def test_zero(self):
        p = Point(10, 20)
        assert translate_point(p, dx=0, dy=0) == p

    def test_immutable(self):
        p = Point(1, 1)
        translate_point(p, dx=10, dy=10)
        assert p == Point(1, 1)


class TestRotatePoint:
    def test_rotate_90_degrees(self):
        result = rotate_point(Point(1, 0), angle=math.pi / 2)
        assert result.x == pytest.approx(0, abs=1e-9)
        assert result.y == pytest.approx(1, abs=1e-9)

    def test_rotate_180_degrees(self):
        result = rotate_point(Point(1, 0), angle=math.pi)
        assert result.x == pytest.approx(-1, abs=1e-9)
        assert result.y == pytest.approx(0, abs=1e-9)

    def test_rotate_360_degrees(self):
        result = rotate_point(Point(3, 4), angle=2 * math.pi)
        assert result.x == pytest.approx(3, abs=1e-9)
        assert result.y == pytest.approx(4, abs=1e-9)

    def test_rotate_around_custom_center(self):
        center = Point(2, 2)
        result = rotate_point(Point(3, 2), angle=math.pi / 2, center=center)
        assert result.x == pytest.approx(2, abs=1e-9)
        assert result.y == pytest.approx(3, abs=1e-9)

    def test_zero_rotation(self):
        p = Point(5, 7)
        result = rotate_point(p, angle=0)
        assert result.x == pytest.approx(5, abs=1e-9)
        assert result.y == pytest.approx(7, abs=1e-9)

    def test_immutable(self):
        p = Point(1, 0)
        rotate_point(p, angle=math.pi / 2)
        assert p == Point(1, 0)

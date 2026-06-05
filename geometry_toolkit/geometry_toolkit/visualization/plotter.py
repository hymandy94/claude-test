import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from collections.abc import Sequence
from ..core.point import Point
from ..core.line import LineSegment


class GeometryPlotter:
    def __init__(self, figsize: tuple[float, float] = (8, 8)):
        self._fig, self._ax = plt.subplots(figsize=figsize)
        self._x_min = float("inf")
        self._x_max = float("-inf")
        self._y_min = float("inf")
        self._y_max = float("-inf")

    def _update_limits(self, points: Sequence[Point]):
        for p in points:
            self._x_min = min(self._x_min, p.x)
            self._x_max = max(self._x_max, p.x)
            self._y_min = min(self._y_min, p.y)
            self._y_max = max(self._y_max, p.y)

    def plot_points(
        self,
        points: Sequence[Point],
        labels: Sequence[str] | None = None,
        color: str = "red",
        marker: str = "o",
        size: int = 50,
    ) -> "GeometryPlotter":
        xs = [p.x for p in points]
        ys = [p.y for p in points]
        self._ax.scatter(xs, ys, c=color, marker=marker, s=size, zorder=5)
        if labels:
            for p, label in zip(points, labels):
                self._ax.annotate(label, (p.x, p.y), textcoords="offset points",
                                  xytext=(5, 5), fontsize=10, color=color)
        self._update_limits(points)
        return self

    def plot_lines(
        self,
        lines: Sequence[LineSegment],
        color: str = "blue",
        linewidth: float = 1.5,
    ) -> "GeometryPlotter":
        for line in lines:
            self._ax.plot(
                [line.start.x, line.end.x],
                [line.start.y, line.end.y],
                color=color,
                linewidth=linewidth,
            )
            self._update_limits([line.start, line.end])
        return self

    def plot_polygon(
        self,
        vertices: Sequence[Point],
        fill: bool = True,
        fill_color: str = "lightblue",
        outline_color: str = "blue",
        outline_width: float = 1.5,
        alpha: float = 0.3,
    ) -> "GeometryPlotter":
        coords = [(p.x, p.y) for p in vertices]
        patch = MplPolygon(
            coords,
            closed=True,
            facecolor=fill_color if fill else "none",
            edgecolor=outline_color,
            linewidth=outline_width,
            alpha=alpha if fill else 1.0,
        )
        self._ax.add_patch(patch)
        self._update_limits(vertices)
        return self

    def plot_polygons(
        self,
        polygons: Sequence[Sequence[Point]],
        fill_colors: Sequence[str] | None = None,
        outline_color: str = "blue",
        alpha: float = 0.3,
    ) -> "GeometryPlotter":
        for i, vertices in enumerate(polygons):
            color = fill_colors[i] if fill_colors and i < len(fill_colors) else None
            self.plot_polygon(vertices, fill_color=color, outline_color=outline_color, alpha=alpha)
        return self

    def set_aspect_equal(self) -> "GeometryPlotter":
        self._ax.set_aspect("equal", adjustable="box")
        return self

    def set_limits(self, x_min: float, x_max: float, y_min: float, y_max: float) -> "GeometryPlotter":
        self._ax.set_xlim(x_min, x_max)
        self._ax.set_ylim(y_min, y_max)
        return self

    def auto_limits(self, padding: float = 0.1) -> "GeometryPlotter":
        if self._x_min == float("inf"):
            self._ax.set_xlim(-1, 1)
            self._ax.set_ylim(-1, 1)
            return self
        dx = self._x_max - self._x_min
        dy = self._y_max - self._y_min
        pad_x = max(dx * padding, 0.5)
        pad_y = max(dy * padding, 0.5)
        self._ax.set_xlim(self._x_min - pad_x, self._x_max + pad_x)
        self._ax.set_ylim(self._y_min - pad_y, self._y_max + pad_y)
        return self

    def save(self, path: str, dpi: int = 150) -> "GeometryPlotter":
        self._fig.savefig(path, dpi=dpi, bbox_inches="tight")
        return self

    def show(self) -> "GeometryPlotter":
        plt.show()
        return self

    def clear(self) -> "GeometryPlotter":
        self._ax.clear()
        self._x_min = float("inf")
        self._x_max = float("-inf")
        self._y_min = float("inf")
        self._y_max = float("-inf")
        return self

# Geometry Toolkit

A Python computational geometry toolkit with core algorithms and visualization support.

## Installation

```bash
pip install -e ".[dev]"
```

## Modules

### Core Algorithms

- **Point**: distance, midpoint, translation, rotation, scaling
- **Line**: line-line intersection, point-to-line distance, line equation
- **Polygon**: point-in-polygon (ray-casting), polygon area (shoelace), convex hull (monotone chain)

### Visualization

- Plot points, line segments, and polygons with matplotlib
- Layered rendering with method chaining
- Save to PNG, SVG, or PDF

## Quick Start

```python
from geometry_toolkit import Point, LineSegment, GeometryPlotter
from geometry_toolkit.core import midpoint, intersect_lines, point_in_polygon, polygon_area

# Points
a = Point(0, 0)
b = Point(3, 4)
print(a.distance_to(b))   # 5.0
print(midpoint(a, b))     # Point(x=1.5, y=2.0)

# Lines
l1 = LineSegment(Point(0, 0), Point(4, 4))
l2 = LineSegment(Point(0, 4), Point(4, 0))
print(intersect_lines(l1, l2))  # Point(x=2.0, y=2.0)

# Polygons
square = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
print(point_in_polygon(Point(1, 1), square))  # True
print(polygon_area(square))                   # 4.0

# Visualization
plotter = GeometryPlotter()
plotter.plot_polygon(square, fill_color="lightgreen")
plotter.plot_points([Point(1, 1)], labels=["A"])
plotter.plot_lines([l1, l2])
plotter.save("example.png")
```

## Tests

```bash
pytest tests/ -v --cov=geometry_toolkit
```

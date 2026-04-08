from __future__ import annotations
import math
from abc import ABC, abstractmethod
from typing import List

# Visitor interface
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") -> str:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> str:
        pass

    @abstractmethod
    def visit_triangle(self, triangle: "Triangle") -> str:
        pass

# Element interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor) -> str:
        pass

# Concrete Elements
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_rectangle(self)

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_triangle(self)

# Concrete Visitors
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        area = math.pi * circle.radius ** 2
        return f"Circle area: {area:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        area = rectangle.width * rectangle.height
        return f"Rectangle area: {area:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        area = 0.5 * triangle.base * triangle.height
        return f"Triangle area: {area:.2f}"

class DrawVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        return f"Drawing Circle with radius {circle.radius:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f"Drawing Rectangle {rectangle.width:.2f} x {rectangle.height:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        return f"Drawing Triangle base {triangle.base:.2f}, height {triangle.height:.2f}"


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4),
    ]

    area_calc = AreaCalculator()
    drawer = DrawVisitor()

    print("Calculating areas:")
    for shape in shapes:
        print(shape.accept(area_calc))

    print("\nDrawing shapes:")
    for shape in shapes:
        print(shape.accept(drawer))

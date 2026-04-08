from abc import ABC, abstractmethod

# Implementor interface
class Color(ABC):
    @abstractmethod
    def apply_color(self) -> str:
        pass

# Concrete Implementors
class RedColor(Color):
    def apply_color(self) -> str:
        return "red"

class BlueColor(Color):
    def apply_color(self) -> str:
        return "blue"

# Abstraction
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self) -> str:
        pass

# Refined Abstractions
class Circle(Shape):
    def draw(self) -> str:
        return f"Drawing Circle with color {self.color.apply_color()}"

class Square(Shape):
    def draw(self) -> str:
        return f"Drawing Square with color {self.color.apply_color()}"


if __name__ == "__main__":
    red = RedColor()
    blue = BlueColor()

    red_circle = Circle(red)
    blue_square = Square(blue)

    print(red_circle.draw())
    print(blue_square.draw())

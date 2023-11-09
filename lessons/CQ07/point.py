"""Defining a Point class."""

from __future__ import annotations


class Point:
    """Creating a Point Class with x and y attributes."""
    x: float
    y: float
    
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """A Constructor."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """String magic method."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Overloads multiplication operator."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, value: int | float) -> Point:
        """Overloads addition operator."""
        return Point(self.x + value, self.y + value)
    
    def scale_by(self, factor: int) -> None:
        """Multiplies x and y by a given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point with scaled x and y attributes by a given factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
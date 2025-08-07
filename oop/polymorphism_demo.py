#!/usr/bin/env python3

"""
A module that demonstrates polymorphism and method overriding in Python.
It defines a base Shape class and two derived classes, Rectangle and Circle,
each with its own implementation of the area() method.
"""

import math

class Shape:
    """
    A base class for all shapes.
    It defines an area() method that must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises an error to ensure subclasses provide their own implementation.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * (self.radius ** 2)

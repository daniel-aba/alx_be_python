#!/usr/bin/env python3

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list of different shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the list and call the area() method on each shape.
    # This demonstrates polymorphism, as the correct area() method is called
    # for each object type (Rectangle and Circle).
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
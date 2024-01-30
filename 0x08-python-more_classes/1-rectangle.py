#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the new Rectangle.

        Args:
            width : The width of the new rectangle (must be a int).
            height : The height of the new rectangle(must be a int).
        """
        self.width = width
        self.height = height

    
    def width(self):
        """Get/set the width of the rectangle."""
        return self.width

   
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    
    def height(self):
        """Get/set the height of the rectangle."""
        return self.height

    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

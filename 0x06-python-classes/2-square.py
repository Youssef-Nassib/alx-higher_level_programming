#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new sqaure"""
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        self.__size = size

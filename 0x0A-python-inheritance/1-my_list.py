#!/usr/bin/python3
"""Defines a list class MyList."""


class MyList(list):
    """printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))

#!/usr/bin/python3
"""Defines a appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of text file.

    
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

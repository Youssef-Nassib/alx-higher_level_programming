#!/usr/bin/python3
"""Defines a text reading function."""


def read_file(filename=""):
    """Print a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

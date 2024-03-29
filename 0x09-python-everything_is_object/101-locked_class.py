#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the  User from instantiating new LockedClass attributes
    for anything .The attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

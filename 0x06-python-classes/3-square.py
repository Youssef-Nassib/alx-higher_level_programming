#!/usr/bin/python3
""" define a class """
class Square:
    def __init__(self, size=0):
        """check if the size in an integer  and must be great than 0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

        """define a new metthode"""
    def area(self):
        """ returne the area """
        return (self.__size * self.__size)

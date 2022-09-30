#!/usr/bin/python3
""" class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from basegeometry"""
    def __init__(self, width, height):
        """ init"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """ string method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

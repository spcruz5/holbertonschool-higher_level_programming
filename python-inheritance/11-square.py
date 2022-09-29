#!/usr/bin/python3
""" Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size):
        """ init"""
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """ area func"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {0}/{0}".format(self.__size)

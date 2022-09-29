#!/usr/bin/python3
""" geometry module"""


class BaseGeometry:
    """ class base Geometry with area func that
    raise an error always it called"""
    def area(self):
        raise Exception("area() is not implemented")

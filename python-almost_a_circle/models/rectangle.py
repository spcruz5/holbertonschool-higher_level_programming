#!/usr/bin/python3
""" Class base"""
from models.base import Base


class Rectangle(Base):
        """ Rectangle class"""
        def __init__(self, width, height, x=0, y=0, id=None):
                """ function that defines the variables"""
                self.__id = super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        @property
        def width(self):
                """ Function that get the width
                Return:
                        private attribute width
                """
                return self.__width

        @property
        def height(self):
                """ Function that get the height
                Return:
                        private attribute height
                """
                return self.__height
        
        @width.setter
        def width(self, value):
                """ Function that set the value of width
                Args:
                        value (int): width
                Raises:
                        TypeError: if value is not int
                        ValueError: if value is less than 0
                """
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self.__width = value

        @height.setter
        def height(self, value):
                """ Function that set the value of height
                Args:
                        value (int): height
                Raises:
                        TypeError: if value is not int
                        ValueError: if value is less than 0
                """
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                self.__height = value
